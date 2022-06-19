<template>
    <div></div>
</template>
<script>
import axios from 'axios';
    export default {
    methods: {
		logout() {
			const path = `http://127.0.0.1:5000/logout`;
			axios.post(path)
				.then(() => {
					window.location = 'http://127.0.0.1:8080';
				})
				.catch((error) => {
                    window.location = 'http://127.0.0.1:8080';
					if(error.response.data.error != null) {
						alert("Error: " + error.response.data.error)
						console.error(error);
						if(error.response.status == 401)
						{window.location = 'http://127.0.0.1:8080/login';}
					}
				});
		},
    },
    created() {
        this.logout();
    },
  }
</script>