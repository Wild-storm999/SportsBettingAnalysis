from sqlalchemy.orm import sessionmaker

import sqlalchemy as db
from models.model import Base
from models.team_models import NCAATeam
from models.team_models import NBATeam
from models.oddshark_models import OddSharkNCAA
from models.oddshark_models import OddSharkNBA
from models.hasla_metrics_model import HaslaMetrics
from models.curated_picks_model import TeamRankingNCAA
from models.curated_picks_model import TeamRankingNBA
from models.curated_picks_model import PicksWiseNCAA
from models.curated_picks_model import PicksWiseNBA
from models.vegas_insider_model import VegasInsider
from models.espn_model import ESPNNCAAB
from models.betql_model import BetQL_NBA
from models.betql_model import BetQL_NCAA
from models.sportsinsights_model import SportsInsightsBETSIGNALS
from models.sportsinsights_model import SportsInsightsBESTBETS
import config
if config.SERVER_ENVIRONMENT:
    engine = db.create_engine(config.SERVER_DATABASE_URI)
else:
    engine = db.create_engine(config.LOCAL_DATABASE_URI)
connection = engine.connect()
if connection:
    print("Database opened successfully")
else:
    print("failed")
Session = sessionmaker(bind=engine)
session = Session()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Created All Tables")


def recreate_team_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[NCAATeam.__table__, NBATeam.__table__])
    Base.metadata.create_all(engine, tables=[NCAATeam.__table__, NBATeam.__table__])
    print("Created Team Tables")


def recreate_oddshark_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[OddSharkNBA.__table__, OddSharkNCAA.__table__])
    Base.metadata.create_all(engine, tables=[OddSharkNBA.__table__, OddSharkNCAA.__table__])
    print("Created OddShark Tables")


def recreate_hasla_metrics_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[HaslaMetrics.__table__])
    Base.metadata.create_all(engine, tables=[HaslaMetrics.__table__])
    print("Created hasla_metrics Tables")


def recreate_curated_picks_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[TeamRankingNCAA.__table__, TeamRankingNBA.__table__,
                                               PicksWiseNCAA.__table__, PicksWiseNBA.__table__])
    Base.metadata.create_all(engine, tables=[TeamRankingNCAA.__table__, TeamRankingNBA.__table__,
                                             PicksWiseNCAA.__table__, PicksWiseNBA.__table__])
    print("Created CuratedPicks Tables")


def recreate_espn_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[ESPNNCAAB.__table__])
    Base.metadata.create_all(engine, tables=[ESPNNCAAB.__table__])
    print("Created ESPN Tables")


def recreate_vegas_insider_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[VegasInsider.__table__])
    Base.metadata.create_all(engine, tables=[VegasInsider.__table__])
    print("Created VegasInsider Tables")


def recreate_betql_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[BetQL_NBA.__table__, BetQL_NCAA.__table__])
    Base.metadata.create_all(engine, tables=[BetQL_NBA.__table__, BetQL_NCAA.__table__])
    print("Created BetQL Tables")


def recreate_sportsinsights_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[SportsInsightsBETSIGNALS.__table__, SportsInsightsBESTBETS.__table__])
    Base.metadata.create_all(engine, tables=[SportsInsightsBETSIGNALS.__table__, SportsInsightsBESTBETS.__table__])
    print("Created SportsInsights Tables")


def close_connection():
    if connection:
        connection.close()
    if session:
        session.close()
