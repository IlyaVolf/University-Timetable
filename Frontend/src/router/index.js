import Vue from "vue";
import VueRouter from "vue-router";
import Shark from "../components/Shark.vue";
import ScheduleHome from "../components/ScheduleHome.vue";
import GamesTest from "../components/GamesTest.vue";
import FacultiesV from "../components/FacultiesV.vue";
import TeachersV from "../components/TeachersV.vue";
import GroupsV from "../components/GroupsV.vue";
import ClassroomsV from "../components/ClassroomsV.vue";
import ConstraintsV from "../components/ConstraintsV.vue";
//import TableOne from "../components/Tables/TableOne.vue";
import TableTwo from "../components/Tables/TableTwo.vue";
import EducationalPrograms from "../components/EducationalPrograms.vue";
import SpecializationsV from "../components/SpecializationsV.vue";


Vue.use(VueRouter);
/* eslint-disable */
const routes = [
  {
    path : '/shark',
    name : 'Shark',
    component : Shark, 
  },
  {
    path : '/shark',
    name : 'Shark',
    component : Shark, 
  },
  {
    path : '/gamestest',
    name : 'GamesTest',
    component : GamesTest, 
  },
  {
    path : '/faculties',
    name : 'FacultiesV',
    component : FacultiesV, 
  },
  {
    path : '/edprograms',
    name : 'EducationalPrograms',
    component : EducationalPrograms, 
  },
  {
    path : '/specializations',
    name : 'SpecializationsV',
    component : SpecializationsV, 
  },
  {
    path : '/classrooms',
    name : 'ClassroomsV',
    component : ClassroomsV, 
  },
  {
    path : '/teachers',
    name : 'TeachersV',
    component : TeachersV, 
  },
  {
    path : '/timetable',
    name : 'TableTwo',
    component : TableTwo, 
  },
  {
    path : '/groups',
    name : 'GroupsV',
    component : GroupsV, 
  },
  {
    path : '/constraints',
    name : 'ConstraintsV',
    component : ConstraintsV, 
  },
  {
    path: '/',
    name: 'schedule',
    component: ScheduleHome,
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
