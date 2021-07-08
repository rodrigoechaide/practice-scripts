# https://mariadb.com/products/skysql/docs/clients/mariadb-connectors/connector-python/
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

# Define the MariaDB engine using MariaDB Connector/Python
DB_USER="test"
DB_PASSWORD="test"
DB_URL="pruebas.cihsn70opsxd.us-east-1.rds.amazonaws.com"
DB_PORT="3306"
DB_NAME="testdb"
DATABASE_URI="mariadb+mariadbconnector://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_URL + ":" + DB_PORT + "/" + DB_NAME

print(DATABASE_URI)

ssl_ca_path = "global-bundle.pem"

engine = sa.create_engine(
    DATABASE_URI,
    connect_args={'ssl_ca': ssl_ca_path}
)

# Get list of Databases
insp = sa.inspect(engine)
db_list = insp.get_schema_names()
print(db_list)