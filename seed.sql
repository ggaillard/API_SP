-- Insérer des utilisateurs
INSERT INTO utilisateurs (id, nom, email) VALUES (1, 'John Doe', 'johndoe@example.com');
INSERT INTO utilisateurs (id, nom, email) VALUES (2, 'Jane Smith', 'janesmith@example.com');
INSERT INTO utilisateurs (id, nom, email) VALUES (3, 'Alice Johnson', 'alicejohnson@example.com');

-- Insérer des abonnements
INSERT INTO abonnements (id, utilisateur_id, service, prix) VALUES (1, 1, 'Netflix', 9.99);
INSERT INTO abonnements (id, utilisateur_id, service, prix) VALUES (2, 1, 'Spotify', 4.99);
INSERT INTO abonnements (id, utilisateur_id, service, prix) VALUES (3, 2, 'Amazon Prime', 12.99);
INSERT INTO abonnements (id, utilisateur_id, service, prix) VALUES (4, 3, 'Disney+', 6.99);