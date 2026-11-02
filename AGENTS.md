# ISTRUZIONI PER GLI AGENTI IA

**STANDARD CORRENTE — REVISIONE 4, 2 NOVEMBRE 2026:** sintesi a due colonne con tutte le righe necessarie e **nessun grassetto**, comprese intestazioni e parole chiave (OpenDyslexic Regular400); interlinea **1,85** come il corpo. **MAPPA CONCETTUALE FINALE** con box tutti **78×78 mm**, sole parole chiave, immagini clay adulte interne **52×29,373 mm**, due colonne e ultimo nodo centrato senza allargarlo. Il limite di cinque righe vale solo per i box discorsivi. La raccolta attiva è di **otto articoli**; il documento ritirato non va ripristinato. Leggere `docs/STANDARD_APPROVATI.md` e `docs/ESCLUSIONE_DOCUMENTO.md`.


## 1. CAPIRE E SELEZIONARE

1. Leggere `README.md`, poi cercare nel catalogo la skill pertinente: `python3 tools/gestisci_skill.py trova "richiesta"`.
2. Leggere il relativo `skills/<nome>/SKILL.md` e soltanto i riferimenti necessari. Non caricare tutte le54 skill né applicarle contemporaneamente.
3. Distinguere **nuovo contenuto**, **manutenzione dell’esistente**, **clonazione in un nuovo progetto**, **solo export**. Per i cloni usare la skill sorgente specifica e non sovrascrivere l’originale.
4. Seguire la richiesta attuale; documenti storici e numeri di deploy non sono istruzioni per ripristinare versioni superate.

## 2. PREPARARE L’AMBIENTE

- Considerare ogni `/home/user/...` un percorso storico, non una prova che il file sia incluso. Per la copia adattata eseguire `tools/gestisci_skill.py prepara` come spiegato nel README.
- Leggere `catalogo/dipendenze-esterne.json` e ispezionare i file necessari. Non inventare sorgenti, account, chiavi o asset mancanti.
- Per una app procurarsi il repository completo autorizzato e seguire README/lockfile locali; la skill da sola non è l’app. L’ambiente di esecuzione può richiedere un’inizializzazione specifica.
- Per documenti fornire testo/PDF e selezionare il modello giusto. Per i media gli strumenti richiamati potrebbero non essere presenti: adattare il flusso agli strumenti disponibili, senza fingere di averli usati.
- Non eseguire tutti gli script per vedere cosa fanno: alcuni modificano file, avviano servizi o preparano deploy. Leggerli prima; usare `--help` solo dopo aver verificato che non ci siano effetti prima del parsing.

## 3. MANTENERE I CONTRATTI

- Per guide del blog leggere `docs/STANDARD_APPROVATI.md` e `quaderno-accessibile`: **IN SINTESI alla fine di ogni unità e MAPPA CONCETTUALE finale** sono obbligatori. Censire le unità reali, non confondere COME SI GIOCA con un riepilogo, aggiungere solo ciò che manca e non duplicare mappe adeguate. Nei bilingui seguire il perimetro corrente: l’articolo inglese di Holland non deve riacquistare la traduzione italiana rimossa. Controllare copertura con `skills/quaderno-accessibile/scripts/verifica_sintesi_mappa.py`. Per mappe/esercizi specialistici applicare il relativo modello; non uniformare indiscriminatamente app, quaderni e mappe.
- Conservare contenuti, enfasi, indice, rimozioni approvate e privacy nelle modifiche grafiche. Non trascrivere diagnosi individuali o dati studenti.
- Conservare le architetture, dashboard, sessioni, accessibilità e PDF dei cloni, cambiando solo ciò che la richiesta autorizza.
- Non rigenerare media approvati durante il collaudo; non correggere a pagamento un risultato senza autorizzazione.
- Nessuna API, generazione a pagamento, pubblicazione o migrazione distruttiva è autorizzata dal semplice clone/installazione di questa raccolta. Richiedere un consenso specifico prima di operazioni conseguenti.

## 4. VERIFICARE E CONSEGNARE

- Fare un checkpoint/diff prima di modificare il progetto selezionato. Lavorare su dati fittizi o ambiente separato, mai resettare sessioni reali.
- Eseguire i test pertinenti e controllare il prodotto effettivo: pagine PDF, audio, viewport desktop/mobile, output del clone. Distinguere controllo sintattico, simulazione e prova reale.
- Non dichiarare conforme PDF/UA, pubblicato o ricostruito identico ciò che non è stato validato realmente.
- Consegnare i file finali e i sorgenti utili; descrivere brevemente cambiamenti e limiti.
- Se si modifica la raccolta, aggiornare catalogo, test e manifest; non conservare vecchi hash come prova di un nuovo pacchetto.

## RISORSE STORICHE E CONFLITTI

Le cartelle `references/originali/` e `shared/INGRESSO_STORICO.md` sono archivio; non prevalgono sulle schede aggiornate. Le skill generali copiate dalla piattaforma conservano il loro contenuto e le attribuzioni; citarle non installa i rispettivi strumenti. Le regole del sistema ospitante restano applicabili.


## PRECEDENZA DELLE RIMOZIONI CORRENTI

Prima di usare un registro storico, leggere `docs/ESCLUSIONE_DOCUMENTO.md`. Non ricostruire il codice05 da vecchi percorsi o allegati. Per gli articoli rimasti leggere `docs/REGISTRO_RACCOLTA_CORRENTE.json` e distinguere cinque riscritture scientifiche, due soli restyling e VR approvata invariata. Non aggiungere quiz o firma Andrea ai due originali. Nelle riscritture il quiz precede la mappa e i riferimenti chiudono il testo. Un aggiornamento di skill non autorizza nuove generazioni, audio, deploy o pubblicazione GitHub.
