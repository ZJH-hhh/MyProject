<template>
    <div class="card edit-field">
        <div class="card-body">
            <label for="edit-post" class="form-label">编辑帖子</label>
            <textarea v-model="content" class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
            <button @click="post" type="button" class="btn btn-primary post-button">发帖</button>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';
import $ from 'jquery';
import { useStore } from 'vuex';

export default {
    name: 'UserProfileWrite',
    setup(props, context) {
        const store = useStore();
        let content = ref('');

        const post = () => {
            $.ajax({
                url: 'https://app165.acapp.acwing.com.cn/myspace/post/',
                type: 'POST',
                data: {
                    content: content.value,
                },
                headers: {
                    'Authorization': 'Bearer ' + store.state.user.access
                },
                success(response) {
                    if (response.result === 'success' && content.value.trim().length !== 0) {
                        context.emit('post', content.value);
                    }
                    content.value = '';
                }
            });
        }

        return {
            content,
            post,
        }
    }
}
</script>

<style scoped>
.edit-field {
    margin-top: 20px;
}

.post-button {
    margin-top: 20px;
}
</style>