from Models.User import User

class Sponsor(User):
    def __init__(self, user_id, name, email, user_status):
        super().__init__(user_id, name, email, user_status)


sponsors = [
    Sponsor("S001", "NovaTech", "contact@novatech.is", "active"),
    Sponsor("S002", "Arctic Systems", "info@arcticsystems.is", "active"),
    Sponsor("S003", "BlueWave Energy", "hello@bluewave.is", "active"),
    Sponsor("S004", "Nordic Data", "support@nordicdata.is", "inactive"),
    Sponsor("S005", "IceSoft Solutions", "team@icesoft.is", "active"),
    Sponsor("S006", "Aurora Labs", "contact@auroralabs.is", "active"),
    Sponsor("S007", "PolarTech", "info@polartech.is", "pending"),
    Sponsor("S008", "FrostByte", "admin@frostbyte.is", "active"),
]