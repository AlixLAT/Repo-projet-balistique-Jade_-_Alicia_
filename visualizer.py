from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class CTrajectoryWidget(QWidget):
    def __init__(self, shots, parent=None):
        super().__init__(parent)
        self._shots = shots

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), Qt.white)

        if not self._shots:
            painter.setPen(QPen(QColor("#444444"), 2))
            painter.drawText(self.rect(), Qt.AlignCenter, "Aucun tir à afficher")
            return

        painter.setPen(QPen(QColor("#444444"), 2))
        painter.drawLine(40, self.height() - 40, self.width() - 40, self.height() - 40)

        max_range = max(shot["portee"] for shot in self._shots)
        max_height = max(shot["hauteur"] for shot in self._shots)
        max_range = max(max_range, 1)
        max_height = max(max_height, 1)

        scale_x = (self.width() - 80) / (max_range * 1.2)
        scale_y = (self.height() - 80) / (max_height * 1.2)

        for index, shot in enumerate(self._shots):
            color = QColor.fromHsl((index * 60) % 360, 180, 60)
            painter.setPen(QPen(color, 2))
            points = []
            steps = 40
            for i in range(steps):
                ratio = i / (steps - 1)
                x = shot["portee"] * ratio
                if shot["portee"] > 0:
                    y = shot["hauteur"] * 4 * (ratio * (1 - ratio))
                else:
                    y = 0
                points.append((x, y))

            for i in range(1, len(points)):
                x1 = 40 + points[i - 1][0] * scale_x
                y1 = self.height() - 40 - points[i - 1][1] * scale_y
                x2 = 40 + points[i][0] * scale_x
                y2 = self.height() - 40 - points[i][1] * scale_y
                painter.drawLine(int(x1), int(y1), int(x2), int(y2))


class CVisualizationWindow(QMainWindow):
    def __init__(self, shots, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Visualisation balistique")
        self.resize(700, 500)

        self._canvas = CTrajectoryWidget(shots)
        self._summary = QLabel(self._build_summary(shots))
        self._summary.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(self._summary)
        layout.addWidget(self._canvas)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def _build_summary(self, shots):
        if not shots:
            return "Aucun tir à visualiser."
        last = shots[-1]
        return (
            f"Dernier tir : vitesse={last['vitesse']} | angle={last['angle']} | "
            f"portée={last['portee']:.2f} | temps={last['temps']:.2f} | hauteur={last['hauteur']:.2f}"
        )


def show_visualization(shots):
    app = QApplication.instance()
    if app is None:
        app = QApplication([])

    window = CVisualizationWindow(shots)
    window.show()
    app.exec_()
