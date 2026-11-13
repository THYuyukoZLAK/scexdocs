(function () {
  'use strict';

  var form = document.getElementById('report-form');
  var submitButton = document.getElementById('submit-button');
  var status = document.getElementById('form-status');

  function setStatus(message, kind) {
    status.textContent = message;
    status.className = 'form-status' + (kind ? ' ' + kind : '');
  }

  form.addEventListener('submit', async function (event) {
    event.preventDefault();
    setStatus('', '');

    if (!form.reportValidity()) {
      setStatus('请完整填写大类、类型、标题、工单内容和有效的 Minecraft ID。', 'error');
      return;
    }

    var data = new FormData(form);
    var payload = {
      category: data.get('category'),
      type: data.get('type'),
      title: data.get('title').trim(),
      content: data.get('content').trim(),
      reporter: data.get('reporter').trim(),
      website: data.get('website')
    };

    submitButton.disabled = true;
    submitButton.textContent = '提交中…';

    try {
      var response = await fetch('/api/bugreport', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      var result = await response.json().catch(function () { return {}; });
      if (!response.ok) throw new Error(result.error || '服务器未能保存工单。');

      form.reset();
      var notification = result.notification;
      var failed = notification === 'failed' || Boolean(notification && typeof notification === 'object' &&
        Object.keys(notification).some(function (key) { return notification[key] === 'failed'; }));
      if (failed) {
        setStatus('工单已保存，但群聊提醒发送失败。工单编号：' + result.id, 'warning');
      } else {
        setStatus('提交成功。工单编号：' + result.id, 'success');
      }
    } catch (error) {
      setStatus(error.message || '提交失败，请稍后重试。', 'error');
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = '提交工单';
    }
  });
}());
