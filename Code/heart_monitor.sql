--Creates a temporary stream.
CREATE OR REPLACE STREAM "TEMP_STREAM" (
	        "HeartRate"        DOUBLE);

-- Sort records by descending anomaly score, insert into output stream
CREATE OR REPLACE PUMP "OUTPUT_PUMP" AS 
   INSERT INTO "TEMP_STREAM"
      SELECT STREAM "HeartRate" FROM "SOURCE_SQL_STREAM_001"
      WHERE "HeartRate" > 70

