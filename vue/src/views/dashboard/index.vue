<template>
  <div class="dashboard-container">
        <el-card class="box-card">
      <div>
            <div class="dashboard-text">角色: {{ my_role }}</div>
    <div class="dashboard-text">用户名: {{ name }}</div>
      </div>
    </el-card>

  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Dashboard",
    data() {
    return {
      my_role: "",
    };
  },
  computed: {
    ...mapGetters(["name", "roles"]),
  },
  mounted: function () {
    this.role(this.roles);
  },
  methods: {
    role(roles) {
      switch (roles) {
        case 0:
          this.my_role = "超级管理员";
          break;
        case 1:
          this.my_role = "普通读者";
          break;
        case 2:
          this.my_role = "采访编目管理员";
          break;
        case 3:
          this.my_role = "采访编目管理员";
          break;
        case 4:
          this.my_role = "流通管理员";
          break;
        case 5:
          this.my_role = "用户管理员";
          break;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
