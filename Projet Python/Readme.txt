  Pour faire fonctionner le code, il convient d’installer la librairie Cherrypy et ses dépendances, et donc de vérifier que l’accès au port requis est possible.
  Pour vérifier cela, regarder le fichier server.conf contenu dans le rendu, une fois les librairies installées et le port libre, lancer le programme.
  Ce dernier doit afficher diverses lignes de code de Cherrypy indiquant le lancement du BUS et la mise en ligne (locale) du serveur.
  L’adresse de connexion de base est 127.0.0.1 :8099, qui dirige au menu principal (index). 
  Dans l’en-tête du code, il y a 3 lignes permettant de rapidement modifier le port utilisé par le serveur.
