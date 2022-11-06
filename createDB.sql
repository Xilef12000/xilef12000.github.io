-- ART definition

CREATE TABLE ART (
	id TEXT(4) NOT NULL, title TEXT NOT NULL, "source" TEXT NOT NULL, "type" TEXT NOT NULL,
	CONSTRAINT ART_PK PRIMARY KEY (id)
);

-- ID definition

CREATE TABLE ID (
	id TEXT(4) NOT NULL,
	"table" TEXT NOT NULL,
	title TEXT,
	CONSTRAINT ID_PK PRIMARY KEY (id)
);

-- PROJECTS definition

CREATE TABLE PROJECTS (
	id TEXT(4) NOT NULL, title TEXT NOT NULL, header TEXT, body TEXT, footer TEXT,
	CONSTRAINT PROJECTS_PK PRIMARY KEY (id)
);

-- "SYSTEM" definition

CREATE TABLE "SYSTEM" (
	id TEXT(4) NOT NULL,
	title TEXT NOT NULL,
	head TEXT,
	header TEXT,
	body TEXT,
	footer TEXT,
	CONSTRAINT SYSTEM_PK PRIMARY KEY (id)
);

-- ART content

INSERT INTO ART (id,title,"source","type") VALUES
	 ('4f35','Rexouium Head','4f35.png','img'),
	 ('b62e','Canine Refsheet','b62e.png','img'),
	 ('d72b','garden seating area daycycle','d72b.html','html'),
	 ('d72c','garden seating area','d72c.png','img'),
	 ('8f58','Meerkat Base','8f58.png','img'),
	 ('8f59','Meerkat Base White Background','8f59.png','img');

-- ID content

INSERT INTO ID (id,"table",title) VALUES
	 ('1082','PROJECTS','xilef12000.github.io'),
	 ('29b7','PROJECTS','Custom Browser Start Page'),
	 ('6497','PROJECTS','WS2821 over Artnet'),
	 ('10a2','PROJECTS','QLC+ Dark Theme'),
	 ('4f35','ART','Rexouium Head'),
	 ('b62e','ART','Canine Refsheet'),
	 ('d72b','ART','garden seating area daycycle'),
	 ('d72c','ART','garden seating area'),
	 ('8f58','ART','Meerkat Base'),
	 ('8f59','ART','Meerkat Base White Background');

-- PROJECTS content

INSERT INTO PROJECTS (id,title,header,body,footer) VALUES
	 ('1082','xilef12000.github.io','simple.html',NULL,'default.html'),
	 ('29b7','Custom Browser Start Page','simple.html','29b7.md','default.html'),
	 ('6497','WS2821 over Artnet','simple.html','6497.md','default.html'),
	 ('10a2','QLC+ Dark Theme','simple.html','10a2.html','default.html');

-- "SYSTEM" content

INSERT INTO "SYSTEM" (id,title,head,header,body,footer) VALUES
	 ('index.html','Home','loadExternal.html','default.html','index.html','default.html'),
	 ('404.html','404 - ERROR',NULL,'simple.html','404.html','default.html'),
	 ('projects.html','Projects',NULL,'simple.html',NULL,'default.html'),
	 ('gallery.html','Gallery','loadExternal.html','simple.html',NULL,'default.html'),
	 ('about.html','About',NULL,'simple.html','about.md','default.html');
