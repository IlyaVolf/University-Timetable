<template>
  <!-- / College Timetable -->
  <div id="timetable">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous" />
    <h5 class="text-center bg-primary text-white" style="border-radius: 10px" v-if="isTeacherSchedule">
      {{ teacherName }}
    </h5><br />
    <h5 class='title' v-if="isGroupSchedule">
      {{ groupNumber }}
    </h5>
    <table width="100%" cellpadding="0" cellspacing="6">
      <tr class="days">
        <th></th>
        <th v-for="day in days" :key="day">{{ day }}</th>
      </tr>
      <tr v-for="(h, i) in hours" :key="i">
        <td class="time">{{ h }}</td>
        <td v-for="(day, j) in days" :key="j">
          <template v-if="isTeacherSchedule">
            <template v-if="
              scheduleTeacherEntities[i][j][0].auditory !== 'null' &&
              scheduleTeacherEntities[i][j][0].groups !== 'null' &&
              scheduleTeacherEntities[i][j][0].subject !== 'null' &&
              scheduleTeacherEntities[i][j][0].typeOfClass !== 'null' &&
              scheduleTeacherEntities[i][j][0].classNumber !== 'null'
            ">
              <span class="auditory">{{ scheduleTeacherEntities[i][j][0].auditory }}</span><br />
              <span class='teacher'>{{ scheduleTeacherEntities[i][j][0].groups }}<br /></span>
               <span class='subject'>{{ scheduleTeacherEntities[i][j][0].subject }}<br /></span>
              <div class='typeSection'><span class='typeOfClass'>{{ scheduleTeacherEntities[i][j][0].typeOfClass }}</span></div><br />
              <!--{{scheduleTeacherEntities[i][j][0].classNumber}}<br>-->
            </template>
          </template>
          <template v-if="isGroupSchedule">
            <template v-if="
              scheduleStudentEntities[i][j][0].auditory !== 'null' &&
              scheduleStudentEntities[i][j][0].teacher !== 'null' &&
              scheduleStudentEntities[i][j][0].subject !== 'null' &&
              scheduleStudentEntities[i][j][0].typeOfClass !== 'null' &&
              scheduleStudentEntities[i][j][0].classNumber !== 'null'
            ">
              <span class='subject'>{{ scheduleStudentEntities[i][j][0].subject }}<br /></span>
              <span class='auditory'> {{ scheduleStudentEntities[i][j][0].auditory }}<br /></span>
              <span class='teacher'> {{ scheduleStudentEntities[i][j][0].teacher }}<br /></span>
              <div class='typeSection'><span class='typeOfClass'>{{ scheduleStudentEntities[i][j][0].typeOfClass }}</span></div><br />
              <!--{{scheduleStudentEntities[i][j][0].classNumber}}<br>-->
            </template>
          </template>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "view-timetable",
  data: () => ({
    days: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    hours: ["9.00", "10.50", "12.40", "14.30", "16.20", "18.10", "20.00"],
    scheduleTeachers: [],
    scheduleTeacherEntities: [],
    teacherName: [],
    scheduleStudents: [],
    scheduleStudentEntities: [],
    groupNumber: [],
    isTeacherSchedule: false,
    isGroupSchedule: false,
    mypath: window.location.href,
  }),
  methods: {
    checkWhichSchedule() {
      if (this.mypath.includes("teachers")) {
        this.isTeacherSchedule = true;
      }
      if (this.mypath.includes("groups")) {
        this.isGroupSchedule = true;
      }
    },
    convertFrontUrlToBackUrl() {
      this.mypath = this.mypath
        .replace("localhost", "127.0.0.1")
        .replace(8080, 5000);
    },
    // 1 GET METHOD
    getGeneratedClasses() {
      const path = this.mypath;
      axios
        .get(path)
        .then((res) => {
          if (this.isTeacherSchedule) {
            this.scheduleTeachers = res.data.scheduleTeachers;
            this.scheduleTeacherEntities =
              this.scheduleTeachers.scheduleEntities;
            this.teacherName = this.scheduleTeachers.entity;
          }
          if (this.isGroupSchedule) {
            this.scheduleStudents = res.data.scheduleStudents;
            this.scheduleStudentEntities =
              this.scheduleStudents.scheduleEntities;
            this.groupNumber = this.scheduleStudents.entity;
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.checkWhichSchedule();
    this.convertFrontUrlToBackUrl();
    this.getGeneratedClasses();
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Open + Sans:300, 400");

$blue: #0085FF;
$purple: #9b59b6;
$navy: #34495e;
$gray: #979797;
$green: #5cc52f;
$red: #e74c3c;
$orange: #f39c12;
$white: #ffffff;
$colors: (
  "blue": $blue,
  "purple": $purple,
  "navy": $navy,
  "green": $green,
  "red": $red,
  "orange": $orange,
  "gray": $gray,
  "white": $white,
);

@each $name,
$color in $colors {
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

.title {
  height: 2em; 
  font-size: 32px;
  vertical-align : middle;
  text-align: center;
}

.auditory {
  color: $navy;
  font-family: SF Pro Rounded;
  font-weight: Semibold;
  font-size: 17px;
  opacity: 1;
  text-align: left;
}

.teacher {
  color: $gray;
  top: 109px;
  left: 0px;
  font-family: SF Pro;
  font-weight: Regular;
  font-size: 14px;
  opacity: 1;
  text-align: left;
  
}

.subject {
  color: $green;
  font-family: SF Pro Display;
  font-weight: Semibold;
  font-size: 16px;
  opacity: 1;
  text-align: left;
}

.typeOfClass {
color: $blue;
font-family:SF Pro Rounded;
font-size:12px;
font-weight:Bold;
height:16px;
left:11px;
right:11px;
letter-spacing:0;
position:absolute;
text-align:center;
width:14px
}

.typeSection {
background-color:rgba(83.00000265240669,187.00000405311584,227.00000166893005,0.30000001192092896);
border-radius:12px;
height:21px;
position: absolute;
width:36px;
text-align: center;
}

body {
  padding: 20px;
}

* {
  box-sizing: border-box;
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
  font-family: SF Pro Rounded;
  font-size: 14px;
  font-weight: Bold;

  tr {
    &:nth-child(2n) {
      background: #eff0f1;
    }

    &:nth-child(2n + 3) {
      background: $white;
    }
  }

  th,
  td {
    padding: 1em;
    width: 10em;
    vertical-align : top;
  }
}

.time {
  background: $gray;
  color: $white;
  text-transform: uppercase;
  font-size: 0.6em;
  text-align: center;
  font-family: SF Pro Rounded;
  font-weight: Bold;
  font-size: 14px;
  opacity: 1;
}

.days {
  background: $green;
  color: $white;
  text-transform: uppercase;
  font-size: 0.6em;
  text-align: center;
  font-family: SF Pro Rounded;
  font-weight: Bold;
  font-size: 14px;

  opacity: 1;
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
  color: $white;
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
  bottom: 100%;
}
</style>