import React from 'react';

function TabellonePunteggi({ punteggio }) {
  return (
    <div className="tabellone-punteggi">
      <h3>Punteggio</h3>
      <p>Utente: {punteggio.utente}</p>
      <p>Sistema: {punteggio.sistema}</p>
    </div>
  );
}

export default TabellonePunteggi;
