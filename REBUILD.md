# RICOSTRUIRE QUESTA RACCOLTA DI SKILL

**STANDARD CORRENTE — REVISIONE 4, 2 NOVEMBRE 2026:** sintesi a due colonne con tutte le righe necessarie e **nessun grassetto**, comprese intestazioni e parole chiave (OpenDyslexic Regular400); interlinea **1,85** come il corpo. **MAPPA CONCETTUALE FINALE** con box tutti **78×78 mm**, sole parole chiave, immagini clay adulte interne **52×29,373 mm**, due colonne e ultimo nodo centrato senza allargarlo. Il limite di cinque righe vale solo per i box discorsivi. La raccolta attiva è di **otto articoli**; il documento ritirato non va ripristinato. Leggere `docs/STANDARD_APPROVATI.md` e `docs/ESCLUSIONE_DOCUMENTO.md`.


1. Estrarre lo ZIP in una cartella nuova oppure clonare il proprio repository. Non servono chiavi API.
2. Usare Python 3.11 o successivo. Il gestore usa solo la libreria standard; per eseguire il validatore YAML e i test delle integrazioni didattiche installare `requirements.txt` in un ambiente virtuale.
3. Lanciare `python3 tools/gestisci_skill.py verifica`. Devono risultare54 skill, nessun errore e tutti gli hash del manifest validi.
4. Lanciare `python3 -m unittest discover -s tests -v`. I test di repository, sintesi/mappe, articoli scientifici ed esclusione sono offline e creano soltanto copie temporanee.
5. Cercare una skill e leggerne il `SKILL.md`: `python3 tools/gestisci_skill.py trova "quiz con audio"`.
6. Per evitare dipendenze dai vecchi percorsi preparare una copia con `python3 tools/gestisci_skill.py prepara --dest ../skills-runtime --workspace ../lavoro`.
7. Procurarsi input e progetti esterni necessari; installare solo le dipendenze della skill scelta. Non eseguire un rendering/clone che si aspetta risorse mancanti.

## NON CONFONDERE TRE VERIFICHE

- **Integrità della raccolta:** manifest, metadati, link attivi, sintassi e preparazione portabile.
- **Esecuzione di una skill:** dipende da input, strumenti, asset e test del caso concreto.
- **Ricostruzione di una app:** richiede anche il suo repository completo, lockfile, configurazione e test/build reali. Questa raccolta non li sostituisce.

## AGGIORNARE IL MANIFEST DOPO MODIFICHE VOLUTE

Verificare prima diff, segreti e test. Poi lanciare `python3 tools/aggiorna_manifest.py` e rieseguire `verifica`. Il manifest è un controllo d’integrità, non una firma crittografica autenticata; l’hash dello ZIP originale consegnato resta un riferimento separato.

