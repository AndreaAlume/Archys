# Archys

## 1. GESTIONE PACCHETTI E SOFTWARE

### Package manager

Fornire all'utente la possibilità di effettuare una ricerca globale, o specifica, dei pacchetti potendoli:
- **installare**
- **disinstallare**
- **aggiornare**: con la possibilità di ***automatizzare*** l'aggiornamento di uno o più pacchetti.

> [!NOTE]
> In aggiunta fornire la possibilità di effettuare il **rollback** alla versione precedente o ad una versione specifica.

L'utente dovrà poter **visualizzare i pacchetti installati**, con opzioni di filtraggio dei risultati (ancora da definire), con le informazioni ritenute utili in maniera chiara e semplice.

Garantire all'utente dei **sistemi di sicurezza** per le installazioni da fonti ritenute non affidabili, automatizzando le procedure di verifica ed evidenziando immediatamente le minacce.

Offrire all'utente la possibilità di **verificare il comportamento del sistema**, isolato e sicuro, a seguito delle operazioni di installazione, aggoirnamento ed eliminazione di uno o più pacchetti effettuate singolarmente o in simultanea.

## 3. BACKUP E SYS-EXPORT
Possibilità di creare backup compressi manuali o automatici di cartelle o file (tramite il percorso cartelle o funzionalità `where`) in una cartella specifica creata e mantenuta dal sistema.
Fornire la possibilità all'utente di decidere quante copie mantenere dei file/cartelle singolarmente.

Tenere un file di backup aggiornato del sistema con i package, informazioni relative al/ai kernel e driver per altre periferiche.

Creare un file (script) da esportare contenente tutte le informazioni e versioni, come package manager installati, ambienti e/o software per configurare una nuova macchina Arch.

## 4. MANUTENZIONE SISTEMA E HARDWARE

**MANUTENZIONE:**
Effettuare in primo luogo una scansione per l'individuazione delle componenti e successivamente controllo hardware periodico (a scelta dell'utente) tramite l'installazione di pacchetti per vedere lo stato di salute dei singoli componenti.

- Tenere aggiornati i driver con delle verifiche periodiche o nel caso di anomalie segnalate dall'utente.
- Gestione tra più kernel con possibilità di switch in caso di malfunzionamenti.
- Migliore visualizzazione dei log (installazioni, crash, servizi) con la possibilità di filtrare i risultati per una ricerca più approfondita e esportarli per un supporto tecnico esterno.

**OTTIMIZZAZIONE:**
Effettuare un'analisi del disco e dello spazio occupato e dare all'utente la possibilità di programmare la pulizia di cartelle.

Creare dei profili energetici attivabili/disattivabili in base alle necessità dell'utente. I profili energetici saranno:
- **Extra power-save**: interventi diretti sulla riduzione del consumo dell'hardware.
- **Power-save**: nessun intervento sulla componente hardware, ma riduzione dei consumi tramite arresto di servizi inutili.
- **Balanced**: bilanciamento delle prestazioni a fronte di un maggiore consumo energetico.
- **High-performance**: il massimo delle prestazioni che la macchina può sprigionare senza tener conto dei consumi energetici.
- **Auto detected**: lasciare a un servizio in background la scelta su quale profilo energetico usare in base alle registrazioni effettuate sull'hardware.

## 5. NETWORKING E SICUREZZA

Fornire all'utente una migliore visibilità delle configurazioni di rete per ethernet, wifi e VPN.

Fornire un layout di configurazione modificabile del firewall semplificato.

Effettuare una scansione di sicurezza generale per evitare le principali minacce conosciute.
