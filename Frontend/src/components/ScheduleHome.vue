<template>
  <body>
<div class="container">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
    <div class="col">
        <a href="/faculties" class="background-cover schedule-menu item_1">
            <span class="name">
                Расписание<br>по факультетам
            </span>
        </a>
    </div>
    <div class="col">
        <a href="/teachers" class="background-cover schedule-menu item_2">
            <span class="name">
                Расписание<br>преподавателей
            </span>
        </a>
    </div>
</div>
</body>
</template>

<script>
export default {
  name: 'ScheduleHome'
};
</script>

<style scoped>
.homeText{
    font-size: 35px;
    color: black;
    text-align: center;
    position: relative;
    top:30px;
    text-shadow: 2px 2px 2px gray;
}

body {
    min-width: 1330px;
    margin-bottom: 620px;
}
</style>
