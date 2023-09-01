<script>
	import '../global.css';
</script>

<svelte:head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  
  <meta name="author" content="Dash Skndash" />
  <meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="icon" href="/favicon.ico" />
  
  <meta property="og:description" content="Take the risk and wait to smile." />
  <meta name="description" content="Take the risk and wait to smile." />

  <meta property="og:image" content="https://jeeq.vercel.app/logo.png" />
  <meta property="og:url" content="https://jeeq.vercel.app/" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:type" content="website" />
  <meta name="twitter:card" content="summary_large_image" />

  <meta name="keywords" content="JEE, Jee study tool, JEE questions, Jee test">
</svelte:head>

<div class="app">
  <header>
    <div>
      <img class="logo" src="logo.png" alt="logo" />
      <h2> Momentum </h2>
    </div>
  </header>
  
	<main>
		<slot />
	</main>
	
	<footer>
	  <span> Source and Credits: Examsnet.com </span>
	  <br>
	  <span> The biggest risk is not taking any risk, take the go and wait to
	  smile. </span>
	  <hr>
	  <span> By Dash Skndash </span>
	</footer>
</div>

<style>
  .app {
    min-height: 100vh;
    width: 100%;
    display: flex;
    flex-direction: column;
  }
  
  header, footer {
    color: #fff;
    padding: .25rem 1rem;
    background: linear-gradient(to right bottom, #dd5410, #ad1616);
  }
  
  header div {
    display: flex;
    align-items: center;
  }
  header .logo {
    width: 2rem;
    height: 2rem;
  }
  
  header {
    box-shadow: 3px 3px 5px rgba(0,0,0,.2);
  }
  footer {
    text-align: center;
    box-shadow: 0 -3px 5px rgba(0,0,0,.2);
  }
  footer span {
    font-size: var(--size-sm);
  }
  footer hr {
    max-width: 10rem;
    margin: .5rem auto;
    border: 1px solid #ff6565;
    border-radius: 1rem;
  }
  main {
    flex-grow: 1;
    padding: 1rem;
  }
</style>
