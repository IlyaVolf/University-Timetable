<template>
    <!-- / College Timetable -->
<div id='timetable'>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
  <table cellpadding='0' cellspacing='0'>
    <tr class="days">
      <th></th>
      <th v-for="day in days" v-bind:key="day">{{day}}</th>
    </tr>
    <tr v-for="(h, i) in hours" :key="i">
      <td class='time'>{{ h }}:00</td>
      <td v-for="(course,index) in timetable[i]" :key="index">
        <span v-if="isObject(course)"></span>
        <div v-if="isArray(course)"></div>
      </td>
    </tr>
    <tr>

      <td class='time'>9.00</td>
      <td class='cs335 blue' data-tooltip='Software Engineering &amp; Software Process'>CS335 [JH1]</td>
      <td class='cs426 purple' data-tooltip='Computer Graphics'>CS426 [CS1]</td>
      <td></td>
      <td></td>
      <td>-</td>
    </tr>
    <tr>
      <td class='time'>10.00</td>
      <td></td>
      <td class='cs335 blue lab' data-tooltip='Software Engineering &amp; Software Process'>CS335 [Lab]</td>
      <td class='md352 green' data-tooltip='Multimedia Production &amp; Management'>MD352 [Kairos]</td>
      <td></td>
      <td>-</td>
    </tr>
    <tr>
      <td class='time'>11.00</td>
      <td></td>
      <td class='cs335 blue lab' data-tooltip='Software Engineering &amp; Software Process'>CS335 [Lab]</td>
      <td class='md352 green' data-tooltip='Multimedia Production &amp; Management'>MD352 [Kairos]</td>
      <td class='cs240 orange' data-tooltip='Operating Systems'>CS240 [CH]</td>
      <td>-</td>
    </tr>
    <tr>
      <td class='time'>12.00</td>
      <td></td>
      <td class='md303 navy' data-tooltip='Media &amp; Globalisation'>MD303 [CS2]</td>
      <td class='md313 red' data-tooltip='Special Topic: Multiculturalism &amp; Nationalism'>MD313 [Iontas]</td>
      <td></td>
      <td>-</td>
    </tr>
    <tr>
      <td class='time'>13.00</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>-</td>
    </tr>
    <tr>
      <td class='time'>14.00</td>
      <td></td>
      <td></td>
      <td class='cs426 purple' data-tooltip='Computer Graphics'>CS426 [CS2]</td>
      <td class='cs240 orange' data-tooltip='Operating Systems'>CS240 [TH1]</td>
      <td>-</td>
    </tr>
    <tr>
      <td class='time'>15.00</td>
      <td></td>
      <td></td>
      <td></td>
      <td class='cs240 orange lab' data-tooltip='Operating Systems'>CS240 [Lab]</td>
      <td>-</td>
    </tr>
    <tr>
      <td class='time'>16.00</td>
      <td></td>
      <td></td>
      <td></td>
      <td class='cs240 orange lab' data-tooltip='Operating Systems'>CS240 [Lab]</td>
      <td>-</td>
    </tr>
    <tr>
      <td class='time'>17.00</td>
      <td class='cs335 blue' data-tooltip='Software Engineering &amp; Software Process'>CS335 [TH1]</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-</td>
    </tr>
  </table>
</div>
</template>

<script>
export default {
	name: 'view-timetable',
	data: () => ({
		days: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
	}),
};
</script>
<style lang="scss">

@import url("https://fonts.googleapis.com/css?family=Open + Sans:300, 400");

$blue: #3498db;
$purple: #9b59b6;
$navy: #34495e;
$green: #2ecc71;
$red: #e74c3c;
$orange: #f39c12;
$colors: (
  "blue": $blue,
  "purple": $purple,
  "navy": $navy,
  "green": $green,
  "red": $red,
  "orange": $orange
);

@each $name, $color in $colors {
  .color-#{$name} {
    background-color: $color;
  }
}

.cs335,
.cs426,
.md303,
.md352,
.md313,
.cs240 {
  font-weight: 300;
  cursor: pointer;
}

body {
  padding: 20px;
}

*,
*:before,
*:after {
  margin: 0;
  padding: 0;
  border: 0;
  outline: 0;
}

table {
  font-family: "Open Sans", Helvetica;
  color: #efefef;

  tr {
    &:nth-child(2n) {
      background: #eff0f1;
    }

    &:nth-child(2n + 3) {
      background: #fff;
    }
  }

  th,
  td {
    padding: 1em;
    width: 10em;
  }
}

.days,
.time {
  background: $navy;
  text-transform: uppercase;
  font-size: 0.6em;
  text-align: center;
}

.time {
  width: 3em !important;
}

// Tooltip Stuff by Chris Bracco
/* Add this attribute to the element that needs a tooltip */
[data-tooltip] {
  position: relative;
  z-index: 2;
  cursor: pointer;
}

/* Hide the tooltip content by default */
[data-tooltip]:before,
[data-tooltip]:after {
  visibility: hidden;
  pointer-events: none;
}

/* Position tooltip above the element */
[data-tooltip]:before {
  position: absolute;
  bottom: 110%;
  left: 50%;
  margin-bottom: 5px;
  margin-left: -80px;
  padding: 7px;
  width: 160px;

  background-color: black;
  color: #fff;
  content: attr(data-tooltip);
  text-align: center;
  font-size: 14px;
  line-height: 1.2;
}

/* Triangle hack to make tooltip look like a speech bubble */
[data-tooltip]:after {
  position: absolute;
  bottom: 110%;
  left: 50%;
  margin-left: -5px;
  width: 0;
  border-top: 5px solid black;
  border-right: 5px solid transparent;
  border-left: 5px solid transparent;
  content: " ";
  font-size: 0;
  line-height: 0;
}

/* Show tooltip content on hover */
[data-tooltip]:hover:before,
[data-tooltip]:hover:after {
  visibility: visible;
  bottom: 90%;
}

</style>