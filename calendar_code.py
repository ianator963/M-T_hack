"""
Make a calendar and use tasks.txt to update due dates
"""
import calendar
import matplotlib.pyplot as plt


calendar.setfirstweekday(6)
w_days = "Sun Mon Tue Wed Thu Fri Sat".split()
m_names = "January February March April May Jun July August September October November December".split()

class MplCalendar(object):
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.cal = calendar.monthcalendar(year, month)
        self.events = [[[] for day in week] for week in self.cal]
    def _mothday_to_index(self, day):
        for week_n, week in enumerate(self.cal):
            try:
                i = week.index(day)
                return week_n, i
            except ValueError:
                pass
        raise ValueError("Not day in calendar")

    def add_event(self, day, event_str):
        week, w_day = self._monthday_to_index(day)
        self.events[week][w_day].append(event_str)

    def show(self):
        'create the calendar'
        f, axs = plt.subplots(len(self.cal), 7, sharex=True, sharey=True)
        for week, ax_row in enumerate(axs):
            for week_day, ax in enumerate(ax_row):
                ax.set_xticks([])
                ax.set_yticks([])
                if self.cal[week][week_day] != 0:
                    ax.text(.02, .98,
                            str(self.cal[week][week_day]),
                            verticalalignment='top',
                            horizontalalignment='left')
                contents = "\n".join(self.events[week][week_day])
                ax.text(.03, .85, contents,
                        verticalalignment='top',
                        horizontalalignment='left',
                        fontsize=9)

        # use the titles of the first row as the weekdays
        for n, day in enumerate(w_days):
            axs[0][n].set_title(day)

        # Place subplots in a close grid
        f.subplots_adjust(hspace=0)
        f.subplots_adjust(wspace=0)
        f.suptitle(m_names[self.month] + ' ' + str(self.year),
                   fontsize=20, fontweight='bold')
        plt.show()
