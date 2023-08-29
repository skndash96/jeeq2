<script>
  import { onMount } from "svelte";
  export let data;
  
  const PREFIX = "https://jeeq-api.vercel.app/getq?";
  const optMap = ['a.', 'b.', 'c.', 'd.', 'e.'];
  
  let history = [],
      cursor = 0;
  
  let sub, klas, chap,
  opt_open = true,
  current_q = null;
  
  $: current_q =  history[cursor];
  
  let show = false;
  
  let pad, pad_stat;
  
  onMount(async () => {
    const el = document.getElementById("sketchpad");
    const Sketchpad = await import("responsive-sketchpad");
    
    pad = new Sketchpad.default(el, {
      width: "300px",
      height: "500px"
    });
    
    pad.setLineColor("#000000");
    pad.setLineSize(2);
    togglePad();
  })

  function undo() {
    pad && pad.undo();
  }
  function clear() {
    pad && pad.clear();
  }
  function togglePad() {
    if (pad) {
      pad_stat = !pad_stat;
      pad.setReadOnly(pad_stat);
    }
  }

  function showAnswer() {
    show = !show;
  }
  function toggleOpt() {
    opt_open = !opt_open;
  }

  async function getQ() {
    show = false;
    
    if (cursor !== 0) {
      cursor = cursor - 1;
      return;
    }
    
    try {
      let res = await
      fetch(`${PREFIX}klas=${klas||""}&sub=${sub||""}&chap=${chap?.toString() || ""}`);
      
      current_q = (await res.json())[0];
      
      history.unshift(current_q);
    } catch (e) {
      console.error(e);
      history.unshift(Error(e.message))
    } finally {
      history = history.slice(0, 5);
    }
  }
  
  function prevQ() {
    cursor = cursor + 1;
  }
</script>



<svelte:head>
  <title>JEE Test</title>
</svelte:head>



<section>
  <div class="titleBox">
    <h1> JEE test </h1>
    
    <button on:click="{toggleOpt}">
      {#if opt_open }
      close
      {:else }
      open
      {/if }
      options
    </button>
  </div>

  <div id="options" class:open={opt_open}>
    <form on:submit|preventDefault="{null}">
      <div>
        <label for="inklas">
          Class
        </label>
        <select id="inklas" bind:value="{klas}">
          <option value="" selected>XI and XII</option>
          <option value="0">XI</option>
          <option value="1">XII</option>
        </select>
      </div>

      <div>
        <label for="insub">
          Subject
        </label>
        <select id="insub" bind:value="{sub}">
          <option value="" selected>All</option>
          <option value="0">Physics</option>
          <option value="1">Chemistry</option>
          <option value="2">Maths</option>
        </select>
      </div>
      
      <div>
        <label for="inchap">
          Chapter
        </label>
        <select id="inchap" bind:value="{chap}" disabed={klas==2 ||sub==3}>
          <option value=""> Any </option>
          {#if klas && sub && klas != 2 && sub != 3}
          {#each data[`${klas}${sub}`] as t, i}
            <option value="{i}"> {t[0]} </option>
          {/each}
          {/if}
        </select>
      </div>
  </form>
</div>

<div class="questionBox">
  <style>.fm-math,fmath{font-family:STIXGeneral,'DejaVu Serif','DejaVu Sans',Times,OpenSymbol,'Standard Symbols L',serif;line-height:1.2}.fm-math mtext,fmath mtext{line-height:normal}.fm-mo,.ma-sans-serif,fmath mi[mathvariant*=sans-serif],fmath mn[mathvariant*=sans-serif],fmath mo,fmath ms[mathvariant*=sans-serif],fmath mtext[mathvariant*=sans-serif]{font-family:STIXGeneral,'DejaVu Sans','DejaVu Serif','Arial Unicode MS','Lucida Grande',Times,OpenSymbol,'Standard Symbols L',sans-serif}.fm-mo-Luc{font-family:STIXGeneral,'DejaVu Sans','DejaVu Serif','Lucida Grande','Arial Unicode MS',Times,OpenSymbol,'Standard Symbols L',sans-serif}.questionsfont{font-family: Arial, sans-serif, STIXGeneral,'DejaVu Sans','DejaVu Serif','Lucida Grande','Arial Unicode MS',Times,OpenSymbol,'Standard Symbols L',sans-serif!important}</style>
  <style>.fm-separator{padding:0 .56ex 0 0}.fm-infix-loose{padding:0 .56ex}.fm-infix{padding:0 .44ex}.fm-prefix{padding:0 .33ex 0 0}.fm-postfix{padding:0 0 0 .33ex}.fm-prefix-tight{padding:0 .11ex 0 0}.fm-postfix-tight{padding:0 0 0 .11ex}.fm-quantifier{padding:0 .11ex 0 .22ex}.ma-non-marking{display:none}.fm-vert,fmath menclose,menclose.fm-menclose{display:inline-block}fmath mrow{white-space:nowrap}.fm-vert{vertical-align:middle}fmath table,fmath tbody,fmath td,fmath tr{border:0!important;padding:0!important;margin:0!important;outline:0!important}fmath table{border-collapse:collapse!important;text-align:center!important;table-layout:auto!important;float:none!important}.fm-frac{padding:0 1px!important}td.fm-den-frac{border-top:solid thin!important}.fm-radicand{padding:0 1px 0 0;border-top:solid;margin-top:.1em}td.fm-underover-base{line-height:1!important}td.fm-mtd{padding:.5ex .4em!important;vertical-align:baseline!important}fmath mphantom{visibility:hidden}fmath menclose[notation=top],menclose.fm-menclose[notation=top]{border-top:solid thin}fmath menclose[notation=right],menclose.fm-menclose[notation=right]{border-right:solid thin}fmath menclose[notation=bottom],menclose.fm-menclose[notation=bottom]{border-bottom:solid thin}fmath menclose[notation=left],menclose.fm-menclose[notation=left]{border-left:solid thin}fmath menclose[notation=box],menclose.fm-menclose[notation=box]{border:thin solid}fmath none{display:none}
  .fm-large-op{font-size:1.3em}.fm-inline .fm-large-op{font-size:1em}.fm-root{font-size:.6em}.fm-script{font-size:.71em}.fm-script .fm-script .fm-script{font-size:1em}</style>
  
  <div>
    {#if current_q === 0}
    Loading...
    {:else if current_q instanceof Error}
      <p class="error">{current_q}</p>
      Something went wrong, try skipping to next
    {:else if current_q}
      {@html `<style>${current_q.styles}</style>`}
      <div>
        <span class="title">
          {current_q.topic}
        </span>
        
        <span>{@html current_q.text}</span>
        
        <hr />
        
        <div class="choice">
          {#if current_q.suggestedAnswer.length > 1}
          {#each current_q.suggestedAnswer as opt, idx}
          <span> {optMap[idx]} {@html opt.text} </span>
          {/each}
          {/if}
        </div>
        <!--Magnetic_Effects_Curr_Mag_116_q-->
        <div class="answer">
          <button on:click="{showAnswer}">
            {#if show} Hide {:else} Show {/if} Answer
          </button> <br />
          
          <span class:shown={show} class="option">
            {#each current_q.acceptedAnswer as opt}
            {optMap[opt.position]} {@html opt.text}
            {/each}
          </span>
        </div>
      </div>
    {:else}
      Press 'Next' for questions
    {/if}
  </div>
</div>

<div class="stateButtons">
  <button class="prevButton" on:click="{prevQ}" disabled={history.length == cursor+1}>
    Previous
  </button>
  
  <button class="nextButton" on:click="{getQ}">
    Next Question
  </button>
</div>

<div class="pad">
  <span> Use this sketchpad for calcs </span>
  <div>
    <button on:click="{undo}"> undo </button>
    <button on:click="{clear}"> clear </button>
    <button on:click="{togglePad}"> {#if pad_stat} unfreeze {:else} freeze {/if} </button>
  </div>
  <div id="blah"></div>
  <div id="sketchpad">
    <div id="padscroll" class:closed={!pad_stat}></div>
  </div>
</div>

</section>



<style>
section {
padding: 2rem .25rem;
margin: auto;
}

@media (min-width: 546px) {
  section {
  max-width: 75vw;
  }
}
@media (min-width: 776px) {
  section {
  max-width: 60vw;
  }
}

.titleBox > * {
display: inline;
margin-right: 1rem;
}
.titleBox h1 {
font-size: 1.5rem;
}
#options {
overflow: hidden;
transform: translateY(-20%);
max-height: 0;
transition: all 250ms ease-out;
}
#options.open {
max-height: 100vh;
transform: translateY(0);
}

form {
padding: .5rem;
margin-top: 2rem;
display: flex;
flex-direction: column;
background: linear-gradient(to left top, #dad1d1, #ecedef);
border-top: 1px solid #000;
border-left: 1px solid #000;
border-radius: 10px;
}

form div {
margin: .5rem 0 .5rem 0;
display: grid;
grid-template-columns: 1fr 2fr;
}

form select {
width: 100%;
}

.questionBox {
padding: 1rem;
margin-top: 2rem;
background: #00000011;
box-shadow: 2px 2px 5px rgba(0,0,0,.2);
}

.questionBox .title {
  font-weight: bold;
  background: rgba(0,0,0,.2);
  display: block;
  transform: translate(-1rem, -1rem);
  padding: .2rem;
}

.questionBox hr {
  margin: 2rem;
}

.questionBox .choice {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.questionBox .answer {
  margin-top: 2rem;
}

.questionBox .option {
  display: none;
}

.questionBox .shown {
  display: inline;
}

.stateButtons {
margin-top: 1rem;
display: flex;
justify-content: space-between;
}
.stateButtons > * {
display: block;
}
.stateButtons button:disabled {
opacity: .9;
}

.pad {
margin-top: 2rem;
}
.pad span {
font-size: .85rem;
}

#padscroll {
position: absolute;
width: 100%;
height: 100%;
}
#padscroll.closed {
max-height: 0;
}

#sketchpad {
margin-top: 1rem;
margin-left: 2rem;
position: relative;
border: 1px solid rgba(0,0,0,.25);
}
</style>