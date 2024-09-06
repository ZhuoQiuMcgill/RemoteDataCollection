document.addEventListener('DOMContentLoaded', function ()
{
    const submitButton = document.getElementById('RunIndexingButton');

    submitButton.addEventListener('click', function ()
    {
        // 获取 textarea 的值
        const prevSentText = document.getElementById('prev_sent_text_input').value;
        const curSentText = document.getElementById('cur_sent_text_input').value;

        // 创建数据对象
        const data = {
            previous: prevSentText,
            current: curSentText
        };

        // 发送 POST 请求到后端
        fetch('/submit_texts/', {  // URL 对应后端视图
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Django 需要 CSRF 令牌
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data =>
            {
                processingData(data)
            })
            .catch((error) =>
            {
                console.error('Error:', error);
                alert('There was an error submitting the texts.');
            });
    });

    // 获取 CSRF 令牌的函数
    function getCookie(name)
    {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '')
        {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++)
            {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '='))
                {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function processingData(data)
    {
        console.log(data);
        const indexed_prev_sent = document.getElementById('indexed_prev_sent');
        const indexed_cur_sent = document.getElementById('indexed_cur_sent');
        indexed_prev_sent.innerHTML = data['indexed_prev_text'];
        indexed_cur_sent.innerHTML = data['indexed_cur_text'];

        const prev_sent_dropdown = document.getElementById('prev_sent_possible_tokens');
        const cur_sent_dropdown = document.getElementById('cur_sent_possible_tokens');
        createDropDown(data['prev_possible_tokens'], prev_sent_dropdown);
        createDropDown(data['cur_possible_tokens'], cur_sent_dropdown);

    }

    function createDropDown(tokens, dropdown)
    {
        dropdown.innerHTML = '';
        tokens.forEach(token => {
            const option = document.createElement('option');
            option.value = token;
            option.text = token;
            dropdown.appendChild(option);
        })
    }
});
