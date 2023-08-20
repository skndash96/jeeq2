<script>
	import '../global.css';
</script>

<div class="app">
  <header>
    <div>
      <h2> Momento </h2>
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
    background: linear-gradient(to right bottom, #a72344, #ad1616);
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
  }
  main {
    flex-grow: 1;
    padding: 1rem;
  }
</style>
