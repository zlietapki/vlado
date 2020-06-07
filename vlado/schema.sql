-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS article;
CREATE TABLE article (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  url TEXT UNIQUE NOT NULL,
  lang TEXT NOT NULL DEFAULT 'ru',
  text TEXT DEFAULT ''
);
INSERT INTO article (url, lang)	VALUES
  ('/ru', 'ru'),

  ('/ru/kosijerevo/igumen-i-monah', 'ru'),
	('/ru/kosijerevo/crkva', 'ru'),
  ('/ru/kosijerevo/kapela', 'ru'),
  ('/ru/kosijerevo/istorija', 'ru'),
  ('/ru/kosijerevo/dogadaji', 'ru'),
  ('/ru/kosijerevo/galereja', 'ru'),
  ('/ru/kosijerevo/kontakt', 'ru'),

  ('/ru/somina/igumen-i-monahinie', 'ru'),
  ('/ru/somina/crkva', 'ru'),
  ('/ru/somina/istorija', 'ru'),
  ('/ru/somina/dogadaji', 'ru'),
  ('/ru/somina/galereja', 'ru'),
  ('/ru/somina/kontakt', 'ru'),

  ('/me', 'me'),

  ('/me/kosijerevo/igumen-i-monah', 'me'),
  ('/me/kosijerevo/crkva', 'me'),
  ('/me/kosijerevo/kapela', 'me'),
  ('/me/kosijerevo/istorija', 'me'),
  ('/me/kosijerevo/dogadaji', 'me'),
  ('/me/kosijerevo/galereja', 'me'),
  ('/me/kosijerevo/kontakt', 'me'),

  ('/me/somina/igumen-i-monahinie', 'me'),
  ('/me/somina/crkva', 'me'),
  ('/me/somina/istorija', 'me'),
  ('/me/somina/dogadaji', 'me'),
  ('/me/somina/galereja', 'me'),
  ('/me/somina/kontakt', 'me');

