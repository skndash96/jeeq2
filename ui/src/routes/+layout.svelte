<script>
	import '../global.css';
</script>

<div class="app">
  <header>
    <div>
      <h2> Folidox </h2>
    </div>
  </header>
  
	<main>
		<slot />
	</main>
	
	<footer>
	  <span> Source and Credits: Examsnet.com </span>
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
  main {
    flex-grow: 1;
    padding: 1rem;
  }
</style>
