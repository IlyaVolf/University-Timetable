<script>
import axios from 'axios';
    export default {
    methods: {
		logout() {
			const path = `http://127.0.0.1:5000/logout`;
			axios.post(path)
				.then(() => {
					this.$route = '/'; 
				})
				.catch((error) => {
					if(error.response.data.error != null) {
						alert("Error: " + error.response.data.error)
						console.error(error);
					}
				});
		},
    }
  }
</script>