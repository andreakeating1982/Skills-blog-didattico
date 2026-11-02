# STANDARD VINCOLANTE — SINTESI SENZA GRASSETTO E MAPPE A BOX STANDARD

## APPROVAZIONE E PRECEDENZA — 2 NOVEMBRE 2026

L’utente ha approvato la mappa di `REALTA_VIRTUALE_A_SCUOLA_MAPPA_BOX_STANDARD_v6.pdf` e ha aggiunto: «Negli specchietti di sintesi non ci devono mai essere parole in grassetto». Queste regole **superano** il modello del 1 novembre con parole chiave Bold, nodi a tutta larghezza e immagini di 37 mm. Le foto storiche restano riferimenti per la tabella, non autorizzano a ripristinare le caratteristiche rifiutate.

L’approvazione stabilisce lo standard per le prossime creazioni/revisioni pertinenti. Una richiesta di aggiornare le skill NON autorizza a rigenerare tutti i PDF, cambiare il PDF approvato o ricostruire lo ZIP completo: consegnare le skill aggiornate, e i documenti solo quando richiesti.

## SPECCHIETTI DI SINTESI — MAI GRASSETTO

- In fondo a **ogni unità tematica** inserire una tabella a **due colonne**: parola chiave / spiegazione. Non un paragrafo in un riquadro.
- Usare **tutte le righe necessarie alla sintesi effettiva**, anche su più pagine; nessun limite di tre/quattro righe o cinque righe tipografiche per questi supporti.
- **TUTTO il testo dello specchietto è OpenDyslexic Regular, font-weight:400**: etichetta IN SINTESI (IN SHORT in inglese), intestazioni, parole chiave, spiegazioni, link ed eventuali note interne. **Nessuna eccezione per i titoli**. Rimuovere i tag `<strong>`/`<b>` solo dentro la sintesi e neutralizzare il Bold ereditato da `<th>`, `<h4>`, classi o CSS inline.
- Parole chiave MAIUSCOLE nel colore dell’unità, spiegazioni nere a sinistra; fascia IN SINTESI con testo bianco maiuscolo centrato, ma **non in grassetto**. Sfondo crema e divisori leggeri, bordo coordinato arrotondato.
- Conservare le spiegazioni effettive della sintesi: **qui le frasi sono ammesse**, mentre nella mappa finale no. Il divieto di grassetto NON comporta eliminare o abbreviare il testo.
- Dimensione uguale al corpo; **interlinea 1,85 nello standard approvato**, identica a quella del corpo e mai compressa. Regola valida per ogni intestazione/cella, non solo i paragrafi.
- Tabella intera quando entra; se lunga, intestazione ripetuta, righe/celle non spezzate, nessuna riduzione tipografica per farla entrare.

## MAPPA CONCETTUALE FINALE — MODELLO APPROVATO REALTÀ VIRTUALE V6

- Titolo esatto **MAPPA CONCETTUALE FINALE**, anche nei documenti bilingui. Per distinguere le voci nell’indice si può aggiungere · ENGLISH / · ITALIANO, non cambiare il titolo nella pagina.
- **Tutti i box concettuali hanno la stessa misura: 78 × 78 mm (7,8 × 7,8 cm)**, quadrati e uniformi fra mappe e documenti. Mai più larghi né più alti della misura approvata, mai a tutta larghezza o `colspan=2`. Non allungare il box per ospitare testo.
- Disposizione in **due colonne**, spazio orizzontale/verticale 6 mm. Se resta un nodo dispari, centrarlo mantenendo 78 × 78 mm; non estenderlo. Usare più nodi e pagine quando necessario, senza ridurre font/interlinea.
- Titolo, tema e intestazioni di gruppo **centrati, senza riquadri/fasce a tutta larghezza**. I soli box sono i nodi di misura standard. Niente frecce, connettori, alberi grafici o diramazioni.
- Nei nodi **solo poche PAROLE CHIAVE in MAIUSCOLO**, non frasi intere, descrizioni, spiegazioni copiate dagli specchietti o note discorsive. Preferire un breve titolo su una/due righe e una/due espressioni chiave da una–tre parole ciascuna. Esempio conforme: «VR / REALTÀ VIRTUALE / MONDO DIGITALE / IMMERSIONE TOTALE». Non conforme: «Uno scenario generato dal computer che simula il mondo reale».
- Riscrivere editorialmente i soli nodi come parole chiave fedeli all’unità; non applicare troncamenti automatici alle frasi né perdere i dettagli dal corpo o dalle sintesi. Gli esempi di limite di parole sono una guardia tecnica, **non sostituiscono il controllo semantico**: anche una frase breve deve essere respinta.
- Ogni nodo contiene **UNA immagine clay adulta esplicativa interna, 52 × 29,373 mm**, centrata e senza tagli (`object-fit:contain`): più grande del precedente 37 × 20,9 mm. Riusare asset pertinenti già approvati; alt significativo nella lingua del documento. Non generare nuove immagini solo per aggiornare le skill.
- Sfondo crema `#fffaf0`, bordo 1pt nel colore del concetto, angoli 3 mm, padding 4 mm verticale / 3 mm orizzontale. Testi centrati; titolo del nodo colorato e Bold, parole chiave nere Regular secondo il modello approvato. **Il nuovo divieto di grassetto riguarda gli specchietti, non modifica le mappe approvate.**
- Interlinea **1,85** e dimensione uguale al corpo (esempio approvato 13pt; metodologie corpo 14pt). Non ridurre per far entrare i contenuti: distribuire i concetti in altri box/pagine. Verificare misure reali, testo/immagini interni e nessun box spezzato.
- Pagina autonoma dopo le unità e prima delle fonti, salvo ordine approvato di appendici/esempi. Intestazioni con il gruppo, ripetute quando serve. Nessuna immagine nelle fonti o nelle sintesi.

## INVARIANTI E AMBITO

Conservare testo, **neretti del corpo**, privacy, rimozioni approvate, quiz/soluzioni, fonti e figure di apertura. Il divieto di neretto è **locale alle sintesi**, non una normalizzazione globale. Conservare struttura e voci dell’indice, aggiornando solo titolo/destinazioni/numeri automatici delle mappe se necessario. Nei bilingui supporti nelle due lingue, distinti dal testo d’autore.

Il limite di cinque righe vale **solo per i piccoli box discorsivi ordinari**, non per tabelle riepilogative; per le mappe vale la misura standard e il contenuto a parole chiave. Non sovrascrivere modelli specialistici invarianti di esercizi, circolari o presentazioni brevi. Nessuna rigenerazione automatica di audio, app o archivi.

Per l’eventuale artefatto diagonale sabbia nei bordi PDF, usare il renderer a superfici opache separate e chiuse `scripts/render_sfondo_uniforme.py`; non ritoccare lo screenshot né cambiare testo/impaginazione per nascondere il difetto.

## RISORSE E CONTROLLI

- `scripts/specchietti_box.py`: generare sintesi Regular e mappe standard da dati editoriali espliciti; rifiutare frasi lunghe anziché troncarle.
- `scripts/integra_sintesi_mappe.py`: integrazione conservativa in HTML, output nuovo; corpo e neretti esterni invariati.
- `templates/sintesi-mappa/integrazioni.json`: esempio aggiornato con `title` e `keywords` separati; `esempio-completo.html` già integrato.
- `templates/sintesi-mappa/standard-approvato-2026-11-02.json`: misure, tipografia e provenienza del modello approvato.
- `scripts/verifica_specchietti_box.py`: verificare tabella vera, tutte le righe, fine unità, **ogni TextBox di sintesi a peso400**, assenza di `<strong>/<b>`, titolo esatto, immagini, box **78×78mm**, immagini **52mm**, nessuna frammentazione o testo fuori bordo, interlinea e dimensione uguali al corpo.
- `tests/test_integrazioni.py`: test positivi/negativi su Bold ereditato/inline/markup, preservazione enfasi del corpo, dimensioni, nodi dispari, frasi non ammesse e immagini.
- `scripts/verifica_box_semantici.py`: cinque righe SOLO ai box del corpo, escludendo gli antenati `data-support-profile`.

Eseguire i test e controllare il PDF renderizzato; i soli selettori CSS non attestano il peso effettivo del font. Il manifest contiene `unit_ids`, `final_map_ids`, `body_font_size_px`, `body_line_height`, misurati dai paragrafi ordinari (non indice/fonti/vecchie sintesi). Non riciclare vecchi rapporti come prova del nuovo standard. La variante PDF/UA del renderer non equivale a certificazione indipendente.

