from bvp.data.config import db


class DataSource(db.Model):
    """Each data source is a data-providing entity."""

    __tablename__ = "data_sources"

    id = db.Column(db.Integer, primary_key=True)
    # Human-readable label (preferably not starting with a capital letter)
    label = db.Column(db.String(80), default="")
    # The type of data source (e.g. user, forecasting script or scheduling script)
    type = db.Column(db.String(80), default="")
    # The id of the source (can link e.g. to bvp_user table)
    user_id = db.Column(
        db.Integer, db.ForeignKey("bvp_users.id"), nullable=True, unique=True
    )

    user = db.relationship("User", backref=db.backref("data_sources", lazy=True))

    def __init__(self, **kwargs):
        super(DataSource, self).__init__(**kwargs)

    def __repr__(self):
        return "<Data source %r (%s)>" % (self.id, self.label)
