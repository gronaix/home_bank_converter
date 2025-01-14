class HomeBankFields:
    DATE = None
    PAYEE = None
    MEMO = None
    AMOUNT = None
    SIGN = None


class DKBGiroFields(HomeBankFields):
    """
    This is meant to be a mapping from DKB Giro to HomeBank fields
    """

    DATE = u'Buchungstag'
    PAYEE = u"Auftraggeber / Begünstigter"
    MEMO = "Verwendungszweck"
    AMOUNT = "Betrag (EUR)"
    # PAYMODE = "Buchungstext"


class DKBVisaFields(HomeBankFields):
    DATE = u"Belegdatum"
    AMOUNT = u"Betrag (EUR)"
    MEMO = u"Beschreibung"


class VBGiroFields(HomeBankFields):
    DATE = u"Buchungstag"
    AMOUNT = u"Umsatz"
    MEMO = u"Vorgang/Verwendungszweck"
    PAYEE = u"Empfänger/Zahlungspflichtiger"
    SIGN = u" "


class SparkasseFields(HomeBankFields):
    DATE = u"Buchungstag"
    AMOUNT = u"Betrag"
    MEMO = u"Verwendungszweck"
    PAYEE = u"Beguenstigter/Zahlungspflichtiger"


class LHVFields(HomeBankFields):
    DATE = u"Date"
    AMOUNT = u"Amount"
    MEMO = u"Description"
    PAYEE = u"Sender/receiver name"

