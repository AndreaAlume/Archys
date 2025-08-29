# Archys

## 1. GESTIONE PACCHETTI E AGGIORNAMENTI
Aggiornamento completo del sistema e dei package manager installati come Pacman. Con possibilità di impostare degli aggiornamenti automatizzati in determinati giorni e orari.

Possibilità di installare / disinstallare package manager come yay e altri.

Registrazione dell'ultimo log di aggiornamento con versione + data + altre info rilevanti fornendo all'utente di effettuare il rollback alla versione precedente in caso di problemi di incompatibilità.

## 2. GESTIONE SOFTWARE
Installazione di software con la possibilità di scegliere pkg manager dal qualle installare il software con notifica di fine installazione.

Disinstallazione del software relativa sempre al pkg. I software saranno disinstallati ma rimarranno in una cronologia di cestino per 15 giorni con la possibilità di recuperarli.

Ricerca, per pacchetti o globale, dei software da installare senza dover cercare il nome esatto.

Mostrare versione del software, spazio totale occupato e possibilità di scrivere appunti e informazioni personali.

Aggiornamenti dei software e possibilità di temporizzarli in determinati giorni e orari.

Aggiunta repository esterni con possibilità di fare dei pull manuali e se l'utente vorrà determinare ogni quanto tempo controllare lo status della repo per farei dei pull programmati.

## 3. BACKUP E SYS-EXPORT
Possibilità di creare dei backup compressi manuali o automatici di cartelle o file (tramite il percorso cerrtelle o funzionalità *'where'*) in una cartella specifica creata e mantenuta dal sistema.
Fornire la possibilità all'utente di decidere quante copie mantenere dei file/cartelle singolarmente.

Tenere un file di backup aggiornato del sistema con i pkg, informazioni relative al/ai kernel e driver per altre periferiche.

Creare un file (script) da esportare contenente tutte le informazioni e versioni, come pkg manager installati, ambienti e/o software per configurare una nuova macchina Arch.

## 4. MANUTENZIONE SISTEMA E HARDWARE

**MANUTENZIONE:**
Effettuare in primo luogo una scansione per l'individuazione delle componenti e successivamente controllo hardware periodico (a scelta dell'utente) tramite l'installazione di pacchetti per vedere lo stato di salute dei singoli componenti.

- Tenere aggiornati i driver con delle verifiche periodiche o nel caso di anomalie segnalate dall'utente.
- Gestione tra più kernel con possibilità di switch in caso di malfunzionamenti.
- Migliore visualizzazione dei log (installazioni, carsh, servizi).

**OTTIMIZZAZIONE:**
Effettuare un'analisi del disco e dello spazio occupato e dare all'utente una possibilità di programmare la pulizia di cartelle.

Creare dei profili energetici attivabili/disattivabili in base alle necessità dell'utente. I profili energetici saranno:
- Extra power-save: interventi diretti sulla riduzione di consumo dell'hardware.
- Power-save: nessun intervento sulla componente hard, ma riduzione dei consumi tramite arresto di servizi inutili.
- Balanced: bilanciamento delle prestazioni a fronte di un maggiore consumo energetico.
- High-performance: il massimo delle prestazioni che la macchina può sprigionare senza tener conto di consumi energetici.
- Auto detected: lasciare ad un servizio in background la scelta su quale profilo energetico usare in base alle registrazioni effettuate sull'hardware.

## 5. NETWORKING E SICUREZZA

Fornire all'utente una migliore visibilità delle configurazioni di rete per ethernet, wifi e VPN.

Fornire un layout di configurazione modificabile del firewall semplificata.

Effettuare una scansione di sicurezza generale per evitare principali minacce conosciute.
