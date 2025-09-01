# Project design

In questo documento verranno designate la struttura, le strategie architetturali e lo stack tecnologico per la finalità del progetto che dovrà soddisfare specifici requisiti ritenuti fondamentali per la buona riuscita.

I requisiti ritenuti fondamentali sono:

- **integrità** per un sistema solido e maturo
- **sicurezza** del sistema senza causare danni, ma aggiornando l'utente di ogni singolo cambiamento
- **scalabilità** per un'ambiente in rapida crescita come Arch
- **rapidità e facilità di sviluppo**

## Stack tecnologico

Lo stack tecnologico scelto a fronte dei requisiti precedentemente elencati prevederà:

- un **linguaggio** affermanto, veloce in termini di codificabilità e non di performance e infine stabile con ampio supporto
- un **database** integrato e leggero con una facilità garantita grazie ad una comunicazione semplice con il backend
- un'**interfaccia** minimale e intuitiva, ma moderna che abbandoni il concetto di legacy.

A fronte di questi vincoli progettuali le scelte per il progetto saranno: 
- [Python](https://docs.python.org/3/)
- [TinyDB](https://tinydb.readthedocs.io/en/latest/)
- [CustomTkinter](https://customtkinter.tomschimansky.com/documentation/)

### Per contribuire al progetto

Per configurare il vostro ambiente virtuale sarà dunque necessario:

1. Avere una macchina con sopra Arch Linux come OS o in alternativa una macchina virtuale con l'immagine ISO di Arch Linux.

>[!NOTE]
>
> Gli utenti Windows che desiderano contribuire tramite WSL riscontreranno delle limitazioni, poiché WSL non offre tutte le funzionalità di sistema necessarie per lo sviluppo completo del progetto.

***IN REVISIONE...***

## Schema progettuale

![schema](/Structure-Schema.png)

### ROOT WINDOW
Rappresenta la pagina principale e il punto di avvio del programma, assumendo anche il ruolo di ***MAIN PROCESS***. Si occuperà di gestire e instradare le attività, organizzando tutti i PA (*process administrator*) che faranno capo proprio al ***MAIN PROCESS*** e le funzionalità comuni delle diverse aree.

### PROCESS ADMINISTRATOR 
Il process administrator rappresenta la macro area di gestione che si occuperà in primo luogo.

#### GUI MANAGER
Un sotto processo gestirà solamente la parte grafica, posizionamento e layout, e l'interattività/dinamicità dell'area gestionale del PA.

#### ENTRY POINT FUNCTIONS
Questo processo gestirà la comunicazione e l’attivazione di tutte le funzionalità interne e condivise, tramite la configurazione di diversi parametri.

Le **SUB FUNCTIONS** corrisponderanno alle chiamate dei comandi del sistema operativo, restituendo diversi valori di ritorno.

Le **SHARED FUNCTIONS** saranno delle funzionalità condivise riutilizzabili direttamente dall'EPF passando ad esse determinati parametri.

>[!IMPORTANT]
> 
> Le funzioni non comunicheranno direttamente con le altre parti del programma, ma risponderanno unicamente al PA.
> Avremo dunque una comunicazione bidirezionale tra il PA e l'EPF.

#### DATA MANAGER SYSTEM

Il DMS si occuperà di organizzare e scrivere i dati non strutturati in uno schema organizzato di dati che gli verranno passati dal PA. Successivamente verrano restituiti i dati strutturati al PA che a sua volta li passerà al FMO. 

Anche in questo caso avremo una comunicazione bidirezionale, dal PA al DMS e viceversa.

#### FILE MANAGER ORCHESTRATOR

Questo processo si occuperà della creazione e organizzazione delle cartelle e dei file con i dati strutturati al loro interno.
