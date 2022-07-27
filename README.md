# Telegrambot-send-Notifications
bot telegram which sends a notification after a number of sent messages.



J'ai utilisé le gestionnaire de messages pour le contenu texte et une variable globale pour compter le nombre de messages envoyés avant une certaine heure (06h00 dans cet exemple). J'ai utilisé la bibliothèque datetime de python pour obtenir l'heure actuelle de la machine sur laquelle le bot est en cours d'exécution. Si ce nombre est inférieur à 6 (c'est-à-dire que l'heure actuelle est comprise entre 00hs et 06hs), j'incrémente le compteur. Si le compteur atteint 10, j'envoie le message et le réinitialise.
Vous ne devriez pas avoir de problèmes avec la variable globale tant que vous utilisez votre bot sur un seul groupe, car il sera partagé entre tous les chats dans lesquels se trouve le bot. J'ai également décidé de réinitialiser le compteur chaque fois qu'un message est envoyé à temps, pour ne pas garder un vieux compteur. Cela pourrait cependant être résolu de manière plus efficace.

N'oubliez pas non plus de désactiver le paramètre de confidentialité du groupe sur votre bot en utilisant @botfather, afin que votre bot puisse gérer les messages d'un groupe.

* installer la dépendance telebot
