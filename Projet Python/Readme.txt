  Pour faire fonctionner le code, il convient d’installer la librairie Cherrypy et ses dépendances, et donc de vérifier que l’accès au port requis est possible.
  Pour vérifier cela, regarder le fichier server.conf contenu dans le rendu, une fois les librairies installées et le port libre, lancer le programme.
  Ce dernier doit afficher diverses lignes de code de Cherrypy indiquant le lancement du BUS et la mise en ligne (locale) du serveur.
  L’adresse de connexion de base est 127.0.0.1 :8099, qui dirige au menu principal (index). 
  Dans l’en-tête du code, il y a 3 lignes permettant de rapidement modifier le port utilisé par le serveur.
  
  
  
  Projet :
  L'idée de base du projet était la création d'une ébauche d'application, en lien avec la crise sanitaire dûe au COVID-19, notamment au confinement mis en place en France en avril   et mai 2020.
  Le livrable devait contenir la possibilité de se connecter et de créer un compte : Foyer, pour les particuliers; Bénévole pour les bénévoles.
  L'interface était libre, l'usage de Cherrypy à été retenu, permettant la création d'un format plus agréable qu'une simple console.
  La création d'une liste de courses, qui utilisait une liste d'aliments, chaque liste pouvant être mise à jour. Les bases de données étaient de simples documents txt.
  
