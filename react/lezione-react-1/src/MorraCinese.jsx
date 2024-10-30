import React from 'react';

const scelte = ['sasso', 'carta', 'forbice'];

function MorraCinese({ sceltaUtente, setSceltaUtente, sceltaSistema, setSceltaSistema, setPunteggio }) {
  const gestisciSceltaUtente = (scelta) => {
    const sceltaSistema = scelte[Math.floor(Math.random() * 3)];
    setSceltaUtente(scelta);
    setSceltaSistema(sceltaSistema);

    if (scelta === sceltaSistema) {
      return;
    } else if (
      (scelta === 'sasso' && sceltaSistema === 'forbice') ||
      (scelta === 'carta' && sceltaSistema === 'sasso') ||
      (scelta === 'forbice' && sceltaSistema === 'carta')
    ) {
      setPunteggio(prevPunteggio => ({ ...prevPunteggio, utente: prevPunteggio.utente + 1 }));
    } else {
      setPunteggio(prevPunteggio => ({ ...prevPunteggio, sistema: prevPunteggio.sistema + 1 }));
    }
  };

  return (
    <div className="morra-cinese">
      <div className="scelte">
        <button onClick={() => gestisciSceltaUtente('sasso')}>Sasso</button>
        <button onClick={() => gestisciSceltaUtente('carta')}>Carta</button>
        <button onClick={() => gestisciSceltaUtente('forbice')}>Forbice</button>
      </div>
      <div className="risultato">
        <p>Utente: {sceltaUtente}</p>
        <p>Sistema: {sceltaSistema}</p>
      </div>
    </div>
  );
}

export default MorraCinese;
