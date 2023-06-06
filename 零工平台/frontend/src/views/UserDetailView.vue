<template>
  <div class="background">
    <div class="userdetail">
      <el-card>
        <div class="card-header">
          <i class="el-icon-user"></i>
          <div class="title clear">
            <h2 style="font-family: 华文楷体 ;color:lightcoral">个&nbsp;&nbsp;人&nbsp;&nbsp;中&nbsp;&nbsp;心</h2>
          </div>
        </div>
        <div class="card-content">
          <el-row>
            <el-col :xs="24" :sm="8">
              <div class="avatar">
                <img src="../views/users.png" alt="Avatar">
              </div>
            </el-col>
            <el-col :xs="24" :sm="16">
              <el-form label-position="top" style="text-align: center">
                <el-form-item style="font-family: 华文楷体 ;color:lightcoral" label="昵称：">
                  <el-input style="font-family: 华文楷体 " v-model="userData.name" placeholder="请输入昵称"></el-input>
                </el-form-item>
                <el-form-item style="font-family: 华文楷体 ;color:lightcoral" label="邮箱：">
                  <el-input style="font-family: 华文楷体" v-model="userData.email" placeholder="请输入邮箱"></el-input>
                </el-form-item>
                <el-form-item style="font-family: 华文楷体 ;color:lightcoral" label="自我介绍：">
                  <el-input type="textarea" v-model="userData.bio" rows="6" maxlength="" show-word-limit
                    placeholder="请输入自我介绍"></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button class="button" style="font-family: 华文楷体 ;color:greenyellow" type="primary"
                    @click="handleSave">修改</el-button>
                  <el-button class="button" style="font-family: 华文楷体 ;color:greenyellow" type="primary"
                    @click="handleSave">保存</el-button>
                </el-form-item>
              </el-form>
            </el-col>
          </el-row>
        </div>



      </el-card>
    </div>

    <div class="work-list">
      <el-tabs v-model="activeTab">
        <el-tab-pane label="我发布的工作" name="published">
          <table class="table">
            <thead>
              <tr style="font-family: 华文楷体 ;color:lightcoral;font-size:30px">
                <th>类型</th>
                <th>标题</th>
                <th>日期</th>
              </tr>

            </thead>
            <thead>
              <tr style="font-family: 华文楷体 ;color:lightcoral;font-size:30px">
                <th>发布工作</th>
                <th>招聘java程序员</th>
                <th>2023/1/2</th>
              </tr>
            </thead>
            <thead>
              <tr style="font-family: 华文楷体 ;color:lightcoral;font-size:30px">
                <th>发布工作</th>
                <th>招聘保洁</th>
                <th>2023/1/3</th>
              </tr>
            </thead>
            <thead>
              <tr style="font-family: 华文楷体 ;color:lightcoral;font-size:30px">
                <th>发布工作</th>
                <th>招聘测试人员</th>
                <th>2023/1/4</th>
              </tr>
            </thead>
            <thead>
              <tr style="font-family: 华文楷体 ;color:lightcoral;font-size:30px">
                <th>发布工作</th>
                <th>招聘运维人员</th>
                <th>2023/1/5</th>
              </tr>
            </thead>
            <thead>
              <tr style="font-family: 华文楷体 ;color:lightcoral;font-size:30px">
                <th>...</th>
                <th>...</th>
                <th>...</th>
              </tr>
            </thead>
            <!--          <tbody>-->
            <!--            <tr v-for="job in publishedJobs" :key="job.id">-->
            <!--              <td>{{ job.title }}</td>-->
            <!--              <td>{{ job.desc }}</td>-->
            <!--              <td>{{ job.status }}</td>-->
            <!--            </tr>-->
            <!--          </tbody>-->
            <!--        </table>-->
            <!--      </el-tab-pane>-->
            <!--      <el-tab-pane label="我接受的工作" name="accepted">-->
            <!--        <table class="table">-->
            <!--          <thead>-->
            <!--            <tr>-->
            <!--              <th>类型：发布工作</th>-->
            <!--              <th>标题：</th>-->
            <!--              <th>描述：</th>-->
            <!--            </tr>-->
            <!--          </thead>-->
            <!--          <tbody>-->
            <!--            <tr v-for="job in acceptedJobs" :key="job.id">-->
            <!--              <td>{{ job.title }}</td>-->
            <!--              <td>{{ job.desc }}</td>-->
            <!--              <td>{{ job.status }}</td>-->
            <!--            </tr>-->
            <!--          </tbody>-->
          </table>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
import {
  ElCard,
  ElRow,
  ElCol,
  ElForm,
  ElFormItem,
  ElInput,
  ElButton
} from 'element-plus'
import { reactive } from "vue"
import { useStore } from 'vuex';

export default {
  name: 'UserDeatil',
  components: {
    ElCard,
    ElRow,
    ElCol,
    ElForm,
    ElFormItem,
    ElInput,
    ElButton
  },
  setup() {
    const store = useStore();
    const userData = reactive({
      name: store.state.user.username,
      email: '20230101@email.com',
      bio: '**互联网公司招聘经理，专注于人才招聘，致力于为公司挖掘优秀程序员，打造高效稳定的技术团队。',
    })

    const handleSave = () => {
      // 保存用户信息的逻辑代码
      console.log('handleSave')
    }

    return {
      userData,
      handleSave
    }
  }
}
</script>

<style scoped>
html,
body {
  margin: 0;
  height: 100%;
}

.background {
  /*background-color: ghostwhite;*/
  background-size: auto;
  /*heigt:800px;*/
  background: url("../../public/1.png");
  /*background-color: white;*/
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  margin: 0;
  height: 730px;

}

.userdetail {
  background-color: black;
  width: 20%;
  height: 100%;
  left: 1px;
  /*position: absolute;*/
  opacity: 0.5;
  border-radius: 30px;
  box-shadow: 10px 10px 25px darkolivegreen;
  padding: 10px;
  float: left;
}

.card-header {
  display: flex;
  align-items: center;
  font-size: 20px;
}

.card-header i {
  font-size: 28px;
  color: #409EFF;
  margin-right: 10px;
}


.avatar {
  text-align: center;
  margin-bottom: 20px;
}

.avatar img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  object-position: center;
}

.button {
  left: 20px;
  Border-radius: 20px;
  width: 35%;
  height: 12.5%;
  font-size: 20px;
  font-family: 楷体;
  /*background-color: lightgreen;*/
  background-image: linear-gradient(147deg, lightblue 0%, grey 74%);
  border: 1px solid rgba(34, 34, 34, 0.85);
  /*{#background-color: rgba(34, 34, 34, 0.85);#}*/

}

.work-list {
  float: right;
  background-color: black;
  width: 78%;
  height: 100%;
  right: 1px;
  /*position: absolute;*/
  opacity: 0.5;
  border-radius: 30px;
  box-shadow: 10px 10px 25px darkolivegreen;
  padding: 10px
}
</style>