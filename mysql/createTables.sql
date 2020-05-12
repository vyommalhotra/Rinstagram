DROP TABLE IF EXISTS Post;
DROP TABLE IF EXISTS PostComment;
DROP TABLE IF EXISTS PostLike;
DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS FRIEND;
DROP TABLE IF EXISTS login;
DROP TABLE IF EXISTS persongroup;
DROP TABLE IF EXISTS groupname;


CREATE TABLE Post (
	gid BIGINT,
    pid VARCHAR(200) NOT NULL UNIQUE,
    id BIGINT,
    postTimeStamp DATETIME,
    msg TEXT,
    likes FLOAT(10),
    PRIMARY KEY (pid)
);

CREATE TABLE PostComment (
	gid BIGINT,
    pid VARCHAR(200),
    commentTimeStamp DATETIME,
	id BIGINT, 
    msg TEXT
);

CREATE TABLE PostLike (
	gid BIGINT,
    pid VARCHAR(200),
    response VARCHAR(200),
    id BIGINT
);

CREATE TABLE Person (
	gid BIGINT,
    id BIGINT UNIQUE AUTO_INCREMENT,
    username VARCHAR(500) UNIQUE,
    PRIMARY KEY (id)
);

CREATE TABLE Friend (
	id BIGINT NOT NULL,
    friendID BIGINT,
    PRIMARY KEY (id, friendID)
);

CREATE TABLE Login (
	username VARCHAR(500) UNIQUE,
    pw VARCHAR(50),
    PRIMARY KEY (username)
);

CREATE TABLE PersonGroup (
	gid BIGINT NOT NULL,
    id BIGINT NOT NULL,
    PRIMARY KEY (gid, id)
);

CREATE TABLE GroupName (
	gid BIGINT UNIQUE AUTO_INCREMENT,
    groupname VARCHAR(100),
    PRIMARY KEY (gid)
)



