axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

document.addEventListener('DOMContentLoaded', function () {
  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      selectable: true,

      // サーバーからイベントを取得してカレンダーに表示
      events: function (info, successCallback, failureCallback) {
        axios
            .post("/app/eventget/", {
                start_date: info.start.valueOf(),
                end_date: info.end.valueOf(),
            })
            .then((response) => {
                successCallback(response.data);
            })
            .catch((error) => {
                console.error(error);
                alert("イベントの取得に失敗しました");
                failureCallback(error);
            });
    },
      select: function(info) {
        const eventname = prompt("イベントを入力してください")
      if (eventname){
        axios
            .post("/app/eventadd/", {
                start_date: info.start.valueOf(),
                end_date: info.end.valueOf(),
                event_name: eventname,
            })
            .then(() => {
                // イベントの追加
                calendar.addEvent({
                title: eventname,
                start: info.start,
                end: info.end,
                allDay: true,
              });
            })
            .catch(() => {
                // バリデーションエラーなど
                console.error(error);
                alert("登録に失敗しました");
            });
      }
    }
  });

  calendar.render();
});
