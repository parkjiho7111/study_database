-- UUID primary key 사용
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE users_uuid_name (
  id_name UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100)
);
INSERT INTO users_uuid_name (name) VALUES ('Alice');

SELECT * FROM users_uuid_name;
INSERT INTO users_uuid_name (name)
VALUES
('Alice'),
('Bob'),
('Charlie');

UPDATE users_uuid_name
SET name = 'updated_name'
WHERE id_name = 'cbdddaca-c7a9-42ff-b0ed-8f00dbcd8377';

DELETE FROM users_uuid_name
WHERE id_name = '92ad55b7-94bf-4e1d-9de2-bbdd54833475';