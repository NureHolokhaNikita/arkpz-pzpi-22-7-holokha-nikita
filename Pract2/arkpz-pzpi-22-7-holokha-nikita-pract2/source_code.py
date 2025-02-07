# 1 !OK
class Member:
    def __init__(self, name=None):
        self.name = name


def get_member_name(member):
    if member is None:
        return 'No Member'
    else:
        return member.name


# 1 OK
class NullMember:
    @property
    def name(self):
        return 'No Member'


class Member:
    def __init__(self, name):
        self.name = name


def get_member_name(member):
    return member.name  # більше не перевіряємо None


# 2 !OK
class UserDataService:
    def load_from_db(self, user_id):
        self._connect_to_db()
        # ...
        return user_data

    def _connect_to_db(self):
        # приватна логіка підключення
        pass


# 2 OK
class UserDataService:
    def load_from_db(self, user_id):
        self.__connect_to_db()
        # ...
        return user_data

    def __connect_to_db(self):
        # реалізація стала більш прихованою
        pass


# 3 !OK
class ReportGenerator:
    def __init__(self, report_type):
        self.report_type = report_type

    def generate(self):
        if self.report_type == 'pdf':
            # код генерації PDF
            pass
        elif self.report_type == 'xlsx':
            # код генерації Excel
            pass
        else:
            # інші типи
            pass


# 3 OK
class ReportGenerator:
    def generate(self):
        raise NotImplementedError


class PDFReportGenerator(ReportGenerator):
    def generate(self):
        # реалізація генерації PDF
        pass


class ExcelReportGenerator(ReportGenerator):
    def generate(self):
        # реалізація генерації Excel
        pass
