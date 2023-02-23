#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from datetime import timedelta as td

from holidays.constants import MAY, JUN, JUL, AUG, OCT
from holidays.countries.argentina import AR, ARG, Argentina
from tests.common import TestCase


class TestArgentina(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Argentina)

    def test_country_aliases(self):
        self.assertCountryAliases(Argentina, AR, ARG)

    def test_new_years_day(self):
        self.holidays.observed = False
        self.assertNoHoliday(
            "2010-12-31",
            "2017-01-02",
        )

        self.holidays.observed = True
        self.assertHoliday(
            "2017-01-01",
        )

        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertHoliday(dt)
            self.assertNoHoliday(
                dt + td(days=-1),
                dt + td(days=+1),
            )

    def test_carnival_day(self):
        self.assertHoliday(
            "2016-02-08",
            "2016-02-09",
            "2017-02-27",
            "2017-02-28",
            "2018-02-12",
            "2018-02-13",
        )

    def test_memory_national_day(self):
        self.holidays.observed = False
        self.assertNoHoliday(
            "1907-03-24",
            "2002-03-24",
        )

        self.holidays.observed = True
        self.assertHoliday(
            "2018-03-24",
            "2017-03-24",
            "2016-03-24",
        )

    def test_holy_week_day(self):
        self.assertHoliday(
            "2016-03-24",
            "2016-03-25",
            "2017-04-13",
            "2017-04-14",
            "2018-03-29",
            "2018-03-30",
        )

    def test_malvinas_war_day(self):
        self.assertHoliday(*[f"{year}-04-02" for year in range(1900, 2100)])

    def test_labor_day(self):
        self.holidays.observed = False
        self.assertNoHoliday(
            "2010-04-30",
            "2011-05-02",
        )

        self.holidays.observed = True
        self.assertHoliday(
            "1922-05-01",
        )

        for year in range(1900, 2100):
            dt = date(year, MAY, 1)
            self.assertHoliday(dt)
            self.assertNoHoliday(
                dt + td(days=-1),
                dt + td(days=+1),
            )

    def test_may_revolution_day(self):
        self.holidays.observed = False
        self.assertNoHoliday(
            "1930-05-25",
            "2014-05-25",
        )

        self.holidays.observed = True
        for year in range(1900, 2100):
            dt = date(year, MAY, 25)
            self.assertHoliday(dt)
            self.assertNoHoliday(
                dt + td(days=-1),
                dt + td(days=+1),
            )

    def test_guemes_day(self):
        for year in range(1900, 2100):
            dt = date(year, JUN, 17)
            self.assertHoliday(dt)
            self.assertNoHoliday(
                dt + td(days=-1),
                dt + td(days=+1),
            )

    def test_belgrano_day(self):
        for year in range(1900, 2100):
            dt = date(year, JUN, 20)
            self.assertHoliday(dt)
            self.assertNoHoliday(
                dt + td(days=-1),
                dt + td(days=+1),
            )

    def test_independence_day(self):
        self.holidays.observed = False
        self.assertNoHoliday(
            "2011-07-09",
            "2017-07-09",
        )

        self.holidays.observed = True
        self.assertHoliday(
            "2011-07-09",
            "2017-07-09",
        )

        for year in range(1900, 2100):
            dt = date(year, JUL, 9)
            self.assertHoliday(dt)
            self.assertNoHoliday(
                dt + td(days=-1),
                dt + td(days=+1),
            )

    def test_san_martin_day(self):
        self.holidays.observed = False
        self.assertNoHoliday(
            "1930-08-10",
            "2008-08-10",
        )

        self.holidays.observed = True
        for year in range(1900, 2100):
            dt = date(year, AUG, 17)
            self.assertHoliday(dt)
            self.assertNoHoliday(
                dt + td(days=-1),
                dt + td(days=+1),
            )

    def test_cultural_day(self):
        self.holidays.observed = False
        self.assertNoHoliday(
            "1913-10-12",
            "2014-10-12",
        )

        self.holidays.observed = True
        for year in range(1900, 2100):
            dt = date(year, OCT, 12)
            self.assertHoliday(dt)
            self.assertNoHoliday(
                dt + td(days=-1),
                dt + td(days=+1),
            )

    def test_national_sovereignty_day(self):
        for year in range(1900, 2100):
            dt = date(year, 11, 20)
            if year < 2010:
                self.assertNoHoliday(dt)
            else:
                self.assertHoliday(dt)
                self.assertNoHoliday(
                    dt + td(days=-1),
                    dt + td(days=+1),
                )

    def test_immaculate_conception_day(self):
        self.holidays.observed = False
        self.assertNoHoliday(
            "1940-12-08",
            "2013-12-08",
        )

        self.holidays.observed = True
        for year in range(1900, 2100):
            dt = date(year, 12, 8)
            self.assertHoliday(dt)
            self.assertNoHoliday(
                dt + td(days=-1),
                dt + td(days=+1),
            )

    def test_christmas(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertHoliday(dt)
            self.assertNoHoliday(
                dt + td(days=-1),
                dt + td(days=+1),
            )

    def test_2022(self):
        self.assertHolidays(
            (
                "2022-01-01",
                "Año Nuevo",
            ),
            (
                "2022-02-28",
                "Día de Carnaval",
            ),
            (
                "2022-03-01",
                "Día de Carnaval",
            ),
            (
                "2022-03-24",
                "Día Nacional de la Memoria por la Verdad y la Justicia",
            ),
            (
                "2022-04-02",
                "Día del Veterano y de los Caidos en la Guerra de Malvinas",
            ),
            (
                "2022-04-14",
                "Semana Santa (Jueves Santo)",
            ),
            (
                "2022-04-15",
                "Semana Santa (Viernes Santo)",
            ),
            (
                "2022-04-17",
                "Día de Pascuas",
            ),
            (
                "2022-05-01",
                "Día del Trabajo",
            ),
            (
                "2022-05-25",
                "Día de la Revolución de Mayo",
            ),
            (
                "2022-06-17",
                "Día Pase a la Inmortalidad del General Martín Miguel de "
                "Güemes",
            ),
            (
                "2022-06-20",
                "Día Pase a la Inmortalidad del General D. Manuel Belgrano",
            ),
            (
                "2022-07-09",
                "Día de la Independencia",
            ),
            (
                "2022-08-17",
                "Día Pase a la Inmortalidad del General D. José de San Martin",
            ),
            (
                "2022-10-12",
                "Día del Respeto a la Diversidad Cultural",
            ),
            (
                "2022-11-20",
                "Día Nacional de la Soberanía",
            ),
            (
                "2022-12-08",
                "La Inmaculada Concepción",
            ),
            (
                "2022-12-25",
                "Navidad",
            ),
        )

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                ar = Argentina(language=language)
                self.assertEqual(ar["2022-01-01"], "Año Nuevo")
                self.assertEqual(ar["2022-12-25"], "Navidad")

        run_tests((Argentina.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Argentina.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        ar = Argentina(language=en_us)
        self.assertEqual(ar["2018-01-01"], "New Year's Day")
        self.assertEqual(ar["2022-12-25"], "Christmas")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            ar = Argentina(language=language)
            self.assertEqual(ar["2018-01-01"], "New Year's Day")
            self.assertEqual(ar["2022-12-25"], "Christmas")