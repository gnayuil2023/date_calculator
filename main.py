'''
Gnay 19.08.2024 Kazakhstan
'''

from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QCalendarWidget, QPushButton, QWidget, QHBoxLayout
from PySide6.QtCore import QDate
import sys


class DateCalculator(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和布局
        self.setWindowTitle("日历天数计算器")
        layout = QVBoxLayout()

        # 开始日期选择
        self.start_label = QLabel("选择开始日期：")
        self.start_calendar = QCalendarWidget()
        self.start_calendar.setSelectedDate(QDate.currentDate())

        # 结束日期选择
        self.end_label = QLabel("选择结束日期：")
        self.end_calendar = QCalendarWidget()
        self.end_calendar.setSelectedDate(QDate.currentDate())

        # 计算按钮
        self.calculate_button = QPushButton("计算天数")
        self.calculate_button.clicked.connect(self.calculate_days_difference)

        # 结果显示
        self.result_label = QLabel("天数为：0 天")

        # 布局添加组件
        layout.addWidget(self.start_label)
        layout.addWidget(self.start_calendar)
        layout.addWidget(self.end_label)
        layout.addWidget(self.end_calendar)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_days_difference(self):
        # 获取两个日期
        start_date = self.start_calendar.selectedDate()
        end_date = self.end_calendar.selectedDate()

        # 计算天数差
        days_difference = start_date.daysTo(end_date)
        self.result_label.setText(f"天数为：{abs(days_difference)} 天")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DateCalculator()
    window.show()
    sys.exit(app.exec())