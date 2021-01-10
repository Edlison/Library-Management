<template>
  <div class="dashboard-container">
    <el-card class="box-card-1">
      <div>
        <div class="dashboard-text">角色: {{ my_role }}</div>
        <div class="dashboard-text">用户名: {{ name }}</div>
      </div>
    </el-card>
    <el-row :gutter="24">
      <el-col :span="12">
        <div class="grid-content bg-purple">
          <el-card class="box-card-2">
            <div>
              <i class="el-icon-info"></i>
              <span> 当前预约数量：</span>
              <div class="dashboard-text" style="text-align: center">
                {{ order_num }}
              </div>
            </div>
          </el-card>
        </div>
      </el-col>
      <el-col :span="12"
        ><div class="grid-content bg-purple">
          <div class="grid-content bg-purple">
            <el-card class="box-card-2">
              <div>
                <i class="el-icon-success"></i>
                <span> 当前借书数量：</span>
                <div class="dashboard-text" style="text-align: center">
                  {{ bor_num }}
                </div>
              </div>
            </el-card>
          </div>
        </div></el-col
      >
    </el-row>
    <div class="">
      <el-card class="box-card formData">
        <div slot="header" class="clearfix">
          <span style="color: red; font-weight: bold">超期记录</span>
        </div>
        <div class="text item">
          <el-table
            ref="formTable"
            :data="tables"
            tooltip-effect="dark"
            stripe
            style="width: 100%"
          >
            <el-table-column
              label="序号"
              type="index"
              width="65"
            ></el-table-column>
            <el-table-column label="ISBN" prop="borrow_book_isbn">
            </el-table-column>
            <el-table-column label="书名" prop="borrow_book_name">
            </el-table-column>
            <el-table-column label="应还时间" prop="borrow_end_time">
            </el-table-column>
          </el-table>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import Axios from "axios";
export default {
  name: "Dashboard",
  data() {
    return {
      my_role: "",
      bor_num: 0,
      order_num: 0,
      tables: [],
    };
  },
  computed: {
    ...mapGetters(["name", "roles"]),
  },
  mounted: function () {
    this.role(this.roles);
    this.getdata();
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
    getdata() {
      let _this = this;
      Axios({
        method: "post",
        url: "/api/user/exceed_the_time",
      }).then(function (res) {
        // console.log(res);
        _this.tables = res.data.data;
      });
      Axios({
        method: "post",
        url: "/api/user/get_info",
      }).then(function (res) {
        console.log(res);
        _this.bor_num = res.data.data.user_borrowing;
        _this.order_num = res.data.data.user_reserving;

      });
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
.box-card-1 {
  background: url(../../assets/image/2.jpg);
  background-size: 100%;
  color: #f8f8ff;
  margin-bottom: 20px;
}
.box-card-2 {
  background: url(../../assets/image/1.jpg);
  background-size: 100%;
  color: #f8f8ff;
  margin-bottom: 20px;
}
.formData {
  // background: url(../../assets/image/3.jpg);
  background-size: 100%;
}
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
