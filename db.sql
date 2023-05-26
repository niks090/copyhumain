CREATE TABLE users (
    username Text not null ,
    password TEXT not null
)
ALTER TABLE users(
ADD COLUMN email TEXT;
)