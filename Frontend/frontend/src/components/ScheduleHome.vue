<template>
<body>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
    <div class="container">
        <div class='buttonsView'>
        <button class='button1' onclick="location.href='/schedule/faculties'" type="button">
            <span  class='text'>Faculty schedule</span>
        </button>
        <button class='button2' onclick="location.href='/schedule/teachers'" type="button">
           <span  class='text'>Schedule of teachers</span>
        </button>
        </div>
    </div>
</body>
</template>

<script>
export default {
  name: 'ScheduleHome'
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Open + Sans:300, 400");

.buttonsView {  
    display: block;
    width: 466px;
    height: 188px;
    background: #EAEAEA;
    opacity: 1;
    margin: 0 auto;


    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    box-shadow: 0px 4px 4px rgba(0.8724896907806396, 0.8906185626983643, 0.9208333492279053, 0.25);

}

.button1 {
  
    background-color:rgba(92.00000211596489, 197.0000034570694, 47.0000009983778, 1);
	width:386px;
	height:44px;
    position:relative;
	left:40px;
	top:40px;
	border-top-left-radius:8px;
	border-top-right-radius:8px;
	border-bottom-left-radius:8px;
	border-bottom-right-radius:8px;
    vertical-align: middle;
    align-content: center;
    align-items: center;
    justify-content: center;
}

.button2 {
  
    background-color:rgba(92.00000211596489, 197.0000034570694, 47.0000009983778, 1);
	width:386px;
	height:44px;
    position:relative;
	left:40px;
	top: 64px;
	border-top-left-radius:8px;
	border-top-right-radius:8px;
	border-bottom-left-radius:8px;
	border-bottom-right-radius:8px;
    vertical-align: middle;
    align-content: center;
    align-items: center;
    justify-content: center;
}

.text {
	color:rgba(255, 255, 255, 1);
    font-family:SF Pro Rounded;
    font-size:18px;
    font-weight: Semibold;
	width:106px;
	left:140px;
	top:12px;
	text-align:center;
}


body {
    min-width: 1330px;
    margin-bottom: 620px;
}
</style>
