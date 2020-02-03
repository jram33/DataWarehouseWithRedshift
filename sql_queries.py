import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')


# DROP TABLES
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
user_table_drop = "DROP TABLE IF EXISTS users"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
time_table_drop = "DROP TABLE IF EXISTS time"


# CREATE TABLES
staging_songs_table_create = ("""CREATE TABLE IF NOT EXISTS staging_songs(
                                     num_songs        INT,
                                     artist_id        VARCHAR,
                                     artist_latitude  NUMERIC,
                                     artist_longitude NUMERIC,
                                     artist_location  VARCHAR,
                                     artist_name      VARCHAR,
                                     song_id          VARCHAR,
                                     title            VARCHAR,
                                     duration         NUMERIC,
                                     year             INT
                                 );""")

staging_events_table_create= ("""CREATE TABLE IF NOT EXISTS staging_events(
                                     artist        VARCHAR,
                                     auth          VARCHAR,
                                     firstName     VARCHAR,
                                     gender        CHAR,
                                     itemInSession INT,
                                     lastName      VARCHAR,
                                     length        NUMERIC,
                                     level         VARCHAR,
                                     location      VARCHAR,
                                     method        VARCHAR,
                                     page          VARCHAR,
                                     registration  NUMERIC,
                                     sessionId     INT,
                                     song          VARCHAR,
                                     status        INT,
                                     ts            BIGINT,
                                     userAgent     VARCHAR,
                                     userId        VARCHAR
                                 );""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(
                            song_id   VARCHAR PRIMARY KEY, 
                            title     VARCHAR, 
                            artist_id VARCHAR, 
                            year      INT, 
                            duration  NUMERIC
                        );""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(
                              artist_id VARCHAR PRIMARY KEY, 
                              name      VARCHAR, 
                              location  VARCHAR, 
                              latitude  NUMERIC, 
                              longitude NUMERIC
                          );""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users(
                            user_id    VARCHAR PRIMARY KEY, 
                            first_name VARCHAR, 
                            last_name  VARCHAR, 
                            gender     CHAR, 
                            level      VARCHAR
                        );""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(
                                songplay_id INT IDENTITY(0,1) PRIMARY KEY, 
                                start_time  TIMESTAMP         NOT NULL, 
                                user_id     VARCHAR           NOT NULL, 
                                level       VARCHAR, 
                                song_id     VARCHAR, 
                                artist_id   VARCHAR, 
                                session_id  INT, 
                                location    VARCHAR, 
                                user_agent  VARCHAR
                            );""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
                            start_time TIMESTAMP PRIMARY KEY, 
                            hour       INT, 
                            day        INT,
                            week       INT,
                            month      INT, 
                            year       INT, 
                            weekday    INT
                        );""")


# STAGING TABLES  
staging_songs_copy = ("""copy staging_songs from '{}'
                         credentials 'aws_iam_role={}'
                         region 'us-west-2' 
                         COMPUPDATE OFF STATUPDATE OFF
                         JSON 'auto'
                      """).format(config.get('S3', 'SONG_DATA'), 
                                  config.get('IAM_ROLE', 'ARN'))

staging_events_copy = ("""copy staging_events from '{}'
                          credentials 'aws_iam_role={}'
                          region 'us-west-2' 
                          COMPUPDATE OFF STATUPDATE OFF
                          JSON '{}'""").format(config.get('S3', 'LOG_DATA'),
                                               config.get('IAM_ROLE', 'ARN'),
                                               config.get('S3', 'LOG_JSONPATH'))


# FINAL TABLES
songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")


# QUERY LISTS
create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
