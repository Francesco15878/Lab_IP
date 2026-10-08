from flask import Flask, render_template_string

app = Flask(__name__)

pagina_juego = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rail Control Pro | Juego de Trenes</title>

  <style>
    :root {
      --fondo: #07101f;
      --panel: #111d32;
      --borde: #314b72;
      --texto: #edf6ff;
      --gris: #a9bed6;
      --verde: #38e89a;
      --rojo: #ff5d70;
      --amarillo: #ffd166;
      --azul: #5aabff;
      --riel: #b8c7da;
      --madera: #6e452a;
      --nivel-color: #5aabff;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      min-height: 100vh;
      overflow-x: hidden;
      font-family: Arial, sans-serif;
      color: var(--texto);
      background:
        radial-gradient(circle at 15% 10%, #244f7d 0%, transparent 28%),
        linear-gradient(135deg, var(--fondo), #0b172b);
      transition: background 0.8s ease;
    }

    header {
      width: 100%;
      padding: 16px 5%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 15px;
      border-bottom: 1px solid var(--borde);
      background: rgba(5, 12, 24, 0.85);
      backdrop-filter: blur(8px);
    }

    .logo {
      font-size: 1.45rem;
      font-weight: 900;
      letter-spacing: 0.5px;
    }

    .logo span {
      color: var(--nivel-color);
    }

    .panel-info {
      display: flex;
      flex-wrap: wrap;
      justify-content: flex-end;
      gap: 10px;
    }

    .dato {
      min-width: 105px;
      padding: 8px 12px;
      border: 1px solid var(--borde);
      border-radius: 8px;
      background: var(--panel);
      font-size: 0.88rem;
    }

    .dato strong {
      display: block;
      margin-top: 2px;
      color: var(--nivel-color);
      font-size: 1rem;
    }

    main {
      width: min(1180px, 94%);
      margin: 22px auto 35px;
    }

    .instrucciones {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 20px;
      align-items: center;
      margin-bottom: 18px;
      padding: 18px;
      border: 1px solid var(--borde);
      border-left: 5px solid var(--nivel-color);
      border-radius: 12px;
      background: rgba(17, 29, 50, 0.92);
      transition: border-color 0.5s ease;
    }

    .instrucciones h1 {
      margin-bottom: 6px;
      font-size: clamp(1.35rem, 3vw, 2rem);
    }

    .instrucciones p {
      color: var(--gris);
      max-width: 780px;
    }

    .estado-mision {
      padding: 10px 14px;
      border-radius: 8px;
      background: #0a1325;
      border: 1px solid var(--borde);
      color: var(--amarillo);
      text-align: center;
      font-size: 0.9rem;
    }

    #juego {
      position: relative;
      height: 570px;
      overflow: hidden;
      border: 3px solid var(--borde);
      border-radius: 16px;
      background:
        linear-gradient(rgba(255, 255, 255, 0.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.035) 1px, transparent 1px),
        #18334a;
      background-size: 38px 38px;
      transition: background 0.7s ease, border-color 0.7s ease;
    }

    .sol {
      position: absolute;
      top: 48px;
      right: 170px;
      width: 65px;
      height: 65px;
      border-radius: 50%;
      background: #ffe08a;
      box-shadow: 0 0 50px #ffe08a;
      opacity: 0.85;
      transition: background 0.7s ease, box-shadow 0.7s ease;
    }

    .nube {
      position: absolute;
      width: 110px;
      height: 34px;
      border-radius: 50px;
      background: rgba(235, 250, 255, 0.35);
      animation: nubes 16s linear infinite;
    }

    .nube::before,
    .nube::after {
      content: "";
      position: absolute;
      border-radius: 50%;
      background: inherit;
    }

    .nube::before {
      width: 45px;
      height: 45px;
      left: 18px;
      top: -20px;
    }

    .nube::after {
      width: 60px;
      height: 60px;
      right: 15px;
      top: -30px;
    }

    .nube-1 {
      top: 75px;
      left: -140px;
    }

    .nube-2 {
      top: 165px;
      left: -250px;
      animation-delay: -8s;
      animation-duration: 23s;
      transform: scale(0.72);
    }

    @keyframes nubes {
      from {
        transform: translateX(0);
      }

      to {
        transform: translateX(1450px);
      }
    }

    .montana {
      position: absolute;
      bottom: 0;
      width: 0;
      height: 0;
      border-left: 210px solid transparent;
      border-right: 210px solid transparent;
      border-bottom: 270px solid #1a4a53;
      opacity: 0.75;
    }

    .montana-1 {
      left: -100px;
    }

    .montana-2 {
      right: -100px;
      border-left-width: 270px;
      border-right-width: 270px;
      border-bottom-width: 330px;
      border-bottom-color: #2a3c69;
    }

    .rio {
      position: absolute;
      right: 0;
      bottom: 0;
      width: 33%;
      height: 100%;
      opacity: 0;
      background: linear-gradient(90deg, transparent, rgba(30, 154, 231, 0.65));
      transition: opacity 0.7s ease;
    }

    .arbol {
      position: absolute;
      z-index: 1;
      width: 24px;
      height: 65px;
      background: #704a2b;
      border-radius: 4px;
    }

    .arbol::before {
      content: "";
      position: absolute;
      bottom: 30px;
      left: -20px;
      width: 65px;
      height: 65px;
      border-radius: 50%;
      background: #2c8f56;
      box-shadow:
        20px -18px #347b4f,
        -15px -12px #3aa85b;
    }

    .arbol-1 {
      bottom: 38px;
      left: 80px;
    }

    .arbol-2 {
      bottom: 58px;
      left: 190px;
      transform: scale(0.75);
    }

    .arbol-3 {
      bottom: 55px;
      right: 180px;
      transform: scale(0.9);
    }

    .riel {
      position: absolute;
      z-index: 2;
      height: 27px;
      border-top: 6px solid var(--riel);
      border-bottom: 6px solid var(--riel);
      filter: drop-shadow(0 2px 0 #384452);
    }

    .riel::after {
      content: "";
      position: absolute;
      top: -6px;
      left: 0;
      width: 100%;
      height: 27px;
      background: repeating-linear-gradient(
        90deg,
        transparent 0,
        transparent 23px,
        var(--madera) 24px,
        var(--madera) 31px,
        transparent 32px,
        transparent 48px
      );
      z-index: -1;
    }

    .riel-principal {
      top: 276px;
      left: 0;
      width: 59%;
    }

    .riel-arriba {
      top: 181px;
      left: 52%;
      width: 39%;
      transform: rotate(-21deg);
      transform-origin: left center;
    }

    .riel-abajo {
      top: 370px;
      left: 52%;
      width: 39%;
      transform: rotate(21deg);
      transform-origin: left center;
    }

    .estacion {
      position: absolute;
      z-index: 5;
      width: 128px;
      padding: 8px;
      border: 2px solid #ffffff;
      border-radius: 10px;
      background: #4e382b;
      text-align: center;
      font-weight: bold;
      font-size: 0.87rem;
      box-shadow: 0 0 17px rgba(255, 255, 255, 0.3);
    }

    .estacion::before {
      content: "🚉";
      display: block;
      font-size: 25px;
    }

    .estacion-arriba {
      top: 80px;
      right: 55px;
      border-color: #ff6373;
    }

    .estacion-abajo {
      bottom: 75px;
      right: 55px;
      border-color: #5aaeff;
    }

    .semaforo {
      position: absolute;
      z-index: 6;
      top: 212px;
      left: 43%;
      width: 38px;
      height: 75px;
      padding-top: 8px;
      border: 3px solid #273548;
      border-radius: 7px;
      background: #101723;
    }

    .luz {
      width: 16px;
      height: 16px;
      margin: 3px auto;
      border-radius: 50%;
      background: #4f1c24;
    }

    .luz-roja.activa {
      background: var(--rojo);
      box-shadow: 0 0 17px var(--rojo);
    }

    .luz-verde.activa {
      background: var(--verde);
      box-shadow: 0 0 17px var(--verde);
    }

    .cambio-riel {
      position: absolute;
      z-index: 8;
      top: 243px;
      left: 51%;
      width: 116px;
      min-height: 73px;
      border: 3px solid var(--amarillo);
      border-radius: 11px;
      background: #203656;
      color: #ffffff;
      font-size: 0.88rem;
      font-weight: bold;
      cursor: pointer;
      box-shadow: 0 0 20px rgba(255, 209, 102, 0.45);
      transition: transform 0.2s, background 0.2s, border-color 0.2s;
    }

    .cambio-riel:hover {
      transform: scale(1.04);
      background: #314d77;
    }

    .cambio-riel.arriba {
      border-color: var(--rojo);
      box-shadow: 0 0 22px rgba(255, 93, 112, 0.7);
    }

    .cambio-riel.abajo {
      border-color: var(--azul);
      box-shadow: 0 0 22px rgba(90, 171, 255, 0.7);
    }

    .controles {
      display: grid;
      grid-template-columns: 1fr 1.7fr 1fr;
      gap: 12px;
      align-items: center;
      margin-top: 16px;
      padding: 14px;
      border: 1px solid var(--borde);
      border-radius: 12px;
      background: rgba(17, 29, 50, 0.92);
    }

    .boton-control {
      border: none;
      border-radius: 9px;
      padding: 12px 10px;
      color: white;
      font-size: 0.92rem;
      font-weight: bold;
      cursor: pointer;
      transition: transform 0.15s, filter 0.15s;
    }

    .boton-control:hover {
      transform: translateY(-2px);
      filter: brightness(1.15);
    }

    .freno {
      background: #a52e42;
    }

    .acelerar {
      background: #167d5a;
    }

    .velocimetro {
      text-align: center;
    }

    .velocimetro span {
      display: block;
      margin-bottom: 6px;
      color: var(--gris);
      font-size: 0.85rem;
    }

    .barra {
      width: 100%;
      height: 15px;
      overflow: hidden;
      border: 1px solid var(--borde);
      border-radius: 20px;
      background: #08101e;
    }

    .barra-progreso {
      width: 0%;
      height: 100%;
      border-radius: inherit;
      background: linear-gradient(90deg, var(--verde), var(--amarillo), var(--rojo));
      transition: width 0.12s linear;
    }

    .tren {
      position: absolute;
      z-index: 7;
      top: 247px;
      left: -130px;
      width: 124px;
      height: 66px;
      transform-origin: center center;
    }

    .locomotora {
      position: absolute;
      right: 0;
      bottom: 10px;
      width: 72px;
      height: 40px;
      border: 2px solid #ffb4be;
      border-radius: 9px 15px 5px 5px;
      background: linear-gradient(135deg, #f35366, #9f1d40);
    }

    .locomotora::before {
      content: "";
      position: absolute;
      top: -28px;
      right: 11px;
      width: 22px;
      height: 31px;
      border: 2px solid #ffc6cd;
      border-radius: 5px 5px 0 0;
      background: #c4e9ff;
    }

    .vagon {
      position: absolute;
      left: 0;
      bottom: 10px;
      width: 48px;
      height: 36px;
      border: 2px solid #b2d6ff;
      border-radius: 5px;
      background: #347cd3;
    }

    .rueda {
      position: absolute;
      z-index: 2;
      bottom: 0;
      width: 15px;
      height: 15px;
      border: 3px solid #c6d1e1;
      border-radius: 50%;
      background: #141a24;
    }

    .r1 { left: 11px; }
    .r2 { left: 47px; }
    .r3 { right: 10px; }
    .r4 { right: 48px; }

    .humo {
      position: absolute;
      top: -46px;
      right: 58px;
      font-size: 27px;
      animation: humo 0.85s infinite alternate;
    }

    @keyframes humo {
      from {
        transform: translate(0, 0) scale(0.8);
        opacity: 0.8;
      }

      to {
        transform: translate(15px, -20px) scale(1.3);
        opacity: 0.08;
      }
    }

    .tren-enemigo {
      display: none;
      position: absolute;
      z-index: 4;
      top: 247px;
      right: -130px;
      width: 95px;
      height: 55px;
      transform: scaleX(-1);
    }

    .tren-enemigo.visible {
      display: block;
    }

    .enemigo-cuerpo {
      position: absolute;
      right: 0;
      bottom: 8px;
      width: 65px;
      height: 35px;
      border: 2px solid #ffc568;
      border-radius: 9px;
      background: #d87920;
    }

    .enemigo-vagon {
      position: absolute;
      left: 0;
      bottom: 8px;
      width: 38px;
      height: 32px;
      border: 2px solid #ffd79a;
      border-radius: 4px;
      background: #b85021;
    }

    .mensaje-final {
      display: none;
      position: absolute;
      inset: 0;
      z-index: 30;
      align-items: center;
      justify-content: center;
      padding: 20px;
      background: rgba(3, 8, 18, 0.86);
      text-align: center;
    }

    .mensaje-final.visible {
      display: flex;
    }

    .caja-final {
      width: min(440px, 100%);
      padding: 30px;
      border: 2px solid var(--nivel-color);
      border-radius: 16px;
      background: #111d32;
      box-shadow: 0 0 40px rgba(90, 171, 255, 0.25);
    }

    .caja-final h2 {
      margin-bottom: 12px;
      font-size: 1.9rem;
    }

    .caja-final p {
      margin-bottom: 20px;
      color: var(--gris);
    }

    .reiniciar {
      border: none;
      border-radius: 8px;
      padding: 12px 22px;
      background: var(--nivel-color);
      color: #06111f;
      font-size: 1rem;
      font-weight: bold;
      cursor: pointer;
    }

    @media (max-width: 750px) {
      header {
        flex-direction: column;
        align-items: flex-start;
      }

      .panel-info {
        justify-content: flex-start;
      }

      .instrucciones {
        grid-template-columns: 1fr;
      }

      #juego {
        height: 500px;
      }

      .estacion {
        right: 10px;
        width: 92px;
        font-size: 0.72rem;
      }

      .estacion-arriba {
        top: 58px;
      }

      .estacion-abajo {
        bottom: 56px;
      }

      .cambio-riel {
        left: 48%;
        width: 90px;
        font-size: 0.75rem;
      }

      .semaforo {
        left: 38%;
      }

      .sol {
        right: 105px;
      }
    }
  </style>
</head>

<body>

  <header>
    <div class="logo">Rail<span>Control Pro</span></div>

    <div class="panel-info">
      <div class="dato">
        Nivel
        <strong id="nivel">1</strong>
      </div>

      <div class="dato">
        Puntos
        <strong id="puntos">0</strong>
      </div>

      <div class="dato">
        Combustible
        <strong id="combustible">100%</strong>
      </div>

      <div class="dato">
        Destino
        <strong id="destino">Roja</strong>
      </div>
    </div>
  </header>

  <main>
    <section class="instrucciones">
      <div>
        <h1>Rail Control Pro</h1>
        <p>
          Controla la velocidad y cambia el riel antes de llegar al cruce.
          A mayor nivel, el tren acelera, aparecen nuevos colores y habrá trenes enemigos.
        </p>
      </div>

      <div class="estado-mision" id="mision">
        Llega a la Estación Roja
      </div>
    </section>

    <div id="juego">
      <div class="sol" id="sol"></div>

      <div class="nube nube-1"></div>
      <div class="nube nube-2"></div>

      <div class="montana montana-1"></div>
      <div class="montana montana-2"></div>

      <div class="rio" id="rio"></div>

      <div class="arbol arbol-1"></div>
      <div class="arbol arbol-2"></div>
      <div class="arbol arbol-3"></div>

      <div class="riel riel-principal"></div>
      <div class="riel riel-arriba"></div>
      <div class="riel riel-abajo"></div>

      <div class="estacion estacion-arriba">
        Estación Roja
      </div>

      <div class="estacion estacion-abajo">
        Estación Azul
      </div>

      <div class="semaforo">
        <div class="luz luz-roja" id="luzRoja"></div>
        <div class="luz luz-verde" id="luzVerde"></div>
      </div>

      <button id="cambioRiel" class="cambio-riel arriba">
        RIEL<br>ARRIBA
      </button>

      <div id="tren" class="tren">
        <div class="humo">💨</div>
        <div class="vagon"></div>
        <div class="locomotora"></div>
        <div class="rueda r1"></div>
        <div class="rueda r2"></div>
        <div class="rueda r3"></div>
        <div class="rueda r4"></div>
      </div>

      <div id="trenEnemigo" class="tren-enemigo">
        <div class="enemigo-vagon"></div>
        <div class="enemigo-cuerpo"></div>
      </div>

      <div id="mensajeFinal" class="mensaje-final">
        <div class="caja-final">
          <h2 id="tituloFinal">Fin del juego</h2>
          <p id="textoFinal"></p>
          <button class="reiniciar" onclick="reiniciarJuego()">Jugar de nuevo</button>
        </div>
      </div>
    </div>

    <section class="controles">
      <button class="boton-control freno" id="frenar">
        ⏹ FRENAR
      </button>

      <div class="velocimetro">
        <span>Velocidad: <strong id="velocidadTexto">0 km/h</strong></span>
        <div class="barra">
          <div class="barra-progreso" id="barraVelocidad"></div>
        </div>
      </div>

      <button class="boton-control acelerar" id="acelerar">
        ▶ ACELERAR
      </button>
    </section>
  </main>

  <script>
    const juego = document.getElementById("juego");
    const tren = document.getElementById("tren");
    const trenEnemigo = document.getElementById("trenEnemigo");
    const cambioRiel = document.getElementById("cambioRiel");

    const nivelTexto = document.getElementById("nivel");
    const puntosTexto = document.getElementById("puntos");
    const combustibleTexto = document.getElementById("combustible");
    const destinoTexto = document.getElementById("destino");
    const misionTexto = document.getElementById("mision");

    const velocidadTexto = document.getElementById("velocidadTexto");
    const barraVelocidad = document.getElementById("barraVelocidad");

    const luzRoja = document.getElementById("luzRoja");
    const luzVerde = document.getElementById("luzVerde");

    const mensajeFinal = document.getElementById("mensajeFinal");
    const tituloFinal = document.getElementById("tituloFinal");
    const textoFinal = document.getElementById("textoFinal");

    const sol = document.getElementById("sol");
    const rio = document.getElementById("rio");

    const botonAcelerar = document.getElementById("acelerar");
    const botonFrenar = document.getElementById("frenar");

    const temas = [
      {
        fondo: "#0b172b",
        campo: "#18334a",
        borde: "#314b72",
        color: "#5aabff",
        sol: "#ffe08a",
        brillo: "#ffe08a",
        rio: "0"
      },
      {
        fondo: "#1d102b",
        campo: "#3b2351",
        borde: "#8053a5",
        color: "#d87aff",
        sol: "#ff9dd5",
        brillo: "#ff9dd5",
        rio: "0"
      },
      {
        fondo: "#10291d",
        campo: "#1e5940",
        borde: "#4fa878",
        color: "#58e89f",
        sol: "#d6ff85",
        brillo: "#d6ff85",
        rio: "0"
      },
      {
        fondo: "#2c180d",
        campo: "#6c3c1a",
        borde: "#d38741",
        color: "#ffc25d",
        sol: "#fff0b0",
        brillo: "#ffc25d",
        rio: "0"
      },
      {
        fondo: "#06152d",
        campo: "#0a2f63",
        borde: "#4b94dd",
        color: "#7fd6ff",
        sol: "#b9f0ff",
        brillo: "#7fd6ff",
        rio: "0.5"
      }
    ];

    let nivel = 1;
    let puntos = 0;
    let combustible = 100;

    let rielActual = "arriba";
    let destino = "arriba";

    let posicion = -130;
    let velocidad = 0;
    let aceleracion = 0.018;
    let velocidadMaxima = 2.9;

    let acelerando = false;
    let frenando = false;
    let jugando = true;

    let enemigoActivo = false;
    let posicionEnemigo = 1200;

    let animacion;

    function cambiarTema() {
      const tema = temas[(nivel - 1) % temas.length];

      document.documentElement.style.setProperty("--nivel-color", tema.color);
      document.documentElement.style.setProperty("--fondo", tema.fondo);
      document.documentElement.style.setProperty("--borde", tema.borde);

      document.body.style.background =
        "radial-gradient(circle at 15% 10%, " + tema.campo + " 0%, transparent 32%), " +
        "linear-gradient(135deg, " + tema.fondo + ", #07101a)";

      juego.style.background =
        "linear-gradient(rgba(255,255,255,0.035) 1px, transparent 1px), " +
        "linear-gradient(90deg, rgba(255,255,255,0.035) 1px, transparent 1px), " +
        tema.campo;

      juego.style.backgroundSize = "38px 38px";

      sol.style.background = tema.sol;
      sol.style.boxShadow = "0 0 50px " + tema.brillo;

      rio.style.opacity = tema.rio;
    }

    function actualizarPanel() {
      nivelTexto.textContent = nivel;
      puntosTexto.textContent = puntos;
      combustibleTexto.textContent = Math.max(0, Math.round(combustible)) + "%";

      const kilometros = Math.round(velocidad * 42);
      velocidadTexto.textContent = kilometros + " km/h";

      const porcentajeVelocidad = Math.min((velocidad / velocidadMaxima) * 100, 100);
      barraVelocidad.style.width = porcentajeVelocidad + "%";

      if (destino === "arriba") {
        destinoTexto.textContent = "Roja";
        misionTexto.textContent = "Llega a la Estación Roja";
      } else {
        destinoTexto.textContent = "Azul";
        misionTexto.textContent = "Llega a la Estación Azul";
      }

      luzRoja.classList.remove("activa");
      luzVerde.classList.remove("activa");

      if (destino === "arriba") {
        luzRoja.classList.add("activa");
      } else {
        luzVerde.classList.add("activa");
      }
    }

    function actualizarCambioRiel() {
      cambioRiel.classList.remove("arriba", "abajo");

      if (rielActual === "arriba") {
        cambioRiel.classList.add("arriba");
        cambioRiel.innerHTML = "RIEL<br>ARRIBA";
      } else {
        cambioRiel.classList.add("abajo");
        cambioRiel.innerHTML = "RIEL<br>ABAJO";
      }
    }

    function activarEnemigo() {
      enemigoActivo = nivel >= 4 && Math.random() < 0.55;

      if (enemigoActivo) {
        posicionEnemigo = 1200;
        trenEnemigo.classList.add("visible");
      } else {
        trenEnemigo.classList.remove("visible");
      }
    }

    function cambiarRiel() {
      if (!jugando) return;

      if (posicion > 455) {
        return;
      }

      rielActual = rielActual === "arriba" ? "abajo" : "arriba";
      actualizarCambioRiel();
    }

    cambioRiel.addEventListener("click", cambiarRiel);

    botonAcelerar.addEventListener("mousedown", function () {
      acelerando = true;
    });

    botonAcelerar.addEventListener("mouseup", function () {
      acelerando = false;
    });

    botonAcelerar.addEventListener("mouseleave", function () {
      acelerando = false;
    });

    botonAcelerar.addEventListener("touchstart", function (evento) {
      evento.preventDefault();
      acelerando = true;
    });

    botonAcelerar.addEventListener("touchend", function () {
      acelerando = false;
    });

    botonFrenar.addEventListener("mousedown", function () {
      frenando = true;
    });

    botonFrenar.addEventListener("mouseup", function () {
      frenando = false;
    });

    botonFrenar.addEventListener("mouseleave", function () {
      frenando = false;
    });

    botonFrenar.addEventListener("touchstart", function (evento) {
      evento.preventDefault();
      frenando = true;
    });

    botonFrenar.addEventListener("touchend", function () {
      frenando = false;
    });

    function fisicaVelocidad() {
      if (acelerando && combustible > 0) {
        velocidad += aceleracion;
        combustible -= 0.055 + velocidad * 0.012;
      } else {
        velocidad -= 0.006;
      }

      if (frenando) {
        velocidad -= 0.05;
      }

      if (velocidad < 0) {
        velocidad = 0;
      }

      if (velocidad > velocidadMaxima) {
        velocidad = velocidadMaxima;
      }

      if (combustible < 0) {
        combustible = 0;
      }
    }

    function posicionarTren() {
      tren.style.left = posicion + "px";

      if (posicion < 470) {
        tren.style.top = "247px";
        tren.style.transform = "rotate(0deg)";
      } else {
        const avance = Math.min(posicion - 470, 300);

        if (rielActual === "arriba") {
          tren.style.top = (247 - avance * 0.35) + "px";
          tren.style.transform = "rotate(-21deg)";
        } else {
          tren.style.top = (247 + avance * 0.35) + "px";
          tren.style.transform = "rotate(21deg)";
        }
      }
    }

    function moverEnemigo() {
      if (!enemigoActivo) return;

      posicionEnemigo -= 1.15 + nivel * 0.09;
      trenEnemigo.style.right = (1200 - posicionEnemigo) + "px";

      if (
        Math.abs(posicion - posicionEnemigo) < 85 &&
        posicion > 80 &&
        posicion < 610 &&
        rielActual === "arriba"
      ) {
        terminarJuego("¡Choque con otro tren!", "Un tren enemigo venía por la misma vía.");
      }
    }

    function moverJuego() {
      if (!jugando) return;

      fisicaVelocidad();
      posicion += velocidad;

      if (combustible <= 0 && velocidad <= 0.02 && posicion < 780) {
        terminarJuego(
          "Sin combustible",
          "El tren se detuvo antes de llegar a la estación."
        );
        return;
      }

      posicionarTren();
      moverEnemigo();
      actualizarPanel();

      if (posicion >= 860) {
        revisarLlegada();
        return;
      }

      animacion = requestAnimationFrame(moverJuego);
    }

    function revisarLlegada() {
      cancelAnimationFrame(animacion);

      const velocidadSegura = 1.8 + nivel * 0.08;

      if (rielActual !== destino) {
        terminarJuego(
          "Riel equivocado",
          "El tren llegó a una estación diferente de la indicada."
        );
        return;
      }

      if (velocidad > velocidadSegura) {
        terminarJuego(
          "Demasiada velocidad",
          "Llegaste demasiado rápido a la estación y el tren no pudo detenerse."
        );
        return;
      }

      puntos += 15 + nivel * 5;
      nivel += 1;

      velocidadMaxima += 0.23;
      aceleracion += 0.0025;
      combustible = Math.min(100, combustible + 30);

      destino = Math.random() < 0.5 ? "arriba" : "abajo";

      cambiarTema();
      activarEnemigo();
      actualizarPanel();

      setTimeout(nuevaRonda, 850);
    }

    function nuevaRonda() {
      posicion = -130;
      velocidad = 0;
      rielActual = Math.random() < 0.5 ? "arriba" : "abajo";

      tren.style.left = "-130px";
      tren.style.top = "247px";
      tren.style.transform = "rotate(0deg)";

      actualizarCambioRiel();
      actualizarPanel();
      moverJuego();
    }

    function terminarJuego(titulo, texto) {
      jugando = false;
      cancelAnimationFrame(animacion);

      tituloFinal.textContent = titulo;
      textoFinal.textContent =
        texto +
        " Lograste " + puntos + " puntos y alcanzaste el nivel " + nivel + ".";

      mensajeFinal.classList.add("visible");
    }

    function reiniciarJuego() {
      cancelAnimationFrame(animacion);

      nivel = 1;
      puntos = 0;
      combustible = 100;

      rielActual = "arriba";
      destino = Math.random() < 0.5 ? "arriba" : "abajo";

      posicion = -130;
      velocidad = 0;
      aceleracion = 0.018;
      velocidadMaxima = 2.9;

      acelerando = false;
      frenando = false;
      jugando = true;

      enemigoActivo = false;
      trenEnemigo.classList.remove("visible");

      cambiarTema();
      actualizarCambioRiel();
      actualizarPanel();

      tren.style.left = "-130px";
      tren.style.top = "247px";
      tren.style.transform = "rotate(0deg)";

      mensajeFinal.classList.remove("visible");

      moverJuego();
    }

    cambiarTema();
    actualizarCambioRiel();
    actualizarPanel();
    moverJuego();
  </script>

</body>
</html>
"""


@app.route("/")
def juego_trenes():
    return render_template_string(pagina_juego)


if __name__ == "__main__":
    app.run(debug=True)