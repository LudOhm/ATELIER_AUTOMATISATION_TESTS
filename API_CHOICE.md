# API Choice

- Étudiant : Ludivine PERRIER-BABIN
- API choisie : Agify
- URL base : https://api.agify.io
- Documentation officielle / README : https://agify.io
- Auth : None

- Endpoints testés :
  - GET https://api.agify.io?name=michael
  - GET https://api.agify.io?name=

- Hypothèses de contrat :
  - code HTTP attendu : 200
  - réponse au format JSON
  - champs attendus : name (string), age (int), count (int)

- Limites / rate limiting connu :
  - pas de clé requise
  - limiter les appels pour éviter le spam

- Risques :
  - indisponibilité temporaire
  - timeout réseau