document.addEventListener('DOMContentLoaded', function ()
{
    const submitButton = document.getElementById('RunIndexingButton');
    const mappingButton = document.getElementById('mapping');
    const saveButton = document.getElementById('save');
    const indexed_prev_sent = document.getElementById('indexed_prev_sent');
    const indexed_cur_sent = document.getElementById('indexed_cur_sent');
    const prev_sent_dropdown = document.getElementById('prev_sent_possible_tokens');
    const cur_sent_dropdown = document.getElementById('cur_sent_possible_tokens');
    const mappingContainer = document.getElementById('mapping-container');
    let indexedPrevText = '';
    let indexedCurText = '';

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
        fetch('/submit_texts/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data =>
            {
                if (data['status'] === 'success')
                {
                    processingData(data);
                } else
                {
                    alert(data['message']);
                }

            })
            .catch((error) =>
            {
                console.error('Error:', error);
                alert('There was an error submitting the texts.');
            });
    });

    mappingButton.addEventListener('click', function ()
    {
        let prev_word = prev_sent_dropdown.options[prev_sent_dropdown.selectedIndex].text;
        let cur_word = cur_sent_dropdown.options[cur_sent_dropdown.selectedIndex].text;
        addMapping(prev_word, cur_word);
    });

    saveButton.addEventListener('click', function ()
    {
        const mappingElements = document.querySelectorAll('#mapping-container .mapping-item');

        const mappings = Array.from(mappingElements).map(element => ({
            prev_word: element.getAttribute('prev_word'),
            cur_word: element.getAttribute('cur_word'),
            mapping_data: element.getAttribute('mapping-data'),
        }));

        const data = {
            indexed_prev_text: indexedPrevText,
            indexed_cur_text: indexedCurText,
            mappings: mappings
        }

        fetch('/save-mappings/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data =>
            {
                if (data.success)
                {
                    alert('Mappings saved successfully!');
                } else
                {
                    alert('Failed to save mappings. Please try again.');
                }
            })
            .catch(error =>
            {
                console.error('Error:', error);
            });
    });

    function addMapping(prev_word, cur_word)
    {
        if (prev_word.length == 0 || cur_word.length == 0)
        {
            return;
        }

        const mappingElement = document.createElement('div');
        mappingElement.classList.add('mapping-item'); // 添加类名

        mappingElement.setAttribute('cur_word', cur_word);
        mappingElement.setAttribute('prev_word', prev_word);
        mappingElement.setAttribute('mapping-data', extractIndexes(cur_word, prev_word));

        // 使用一个内部的div包裹文本内容
        const textContent = document.createElement('div');
        textContent.textContent = `${prev_word} → ${cur_word}`;

        // 创建删除按钮
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'x'; // 设置按钮文本
        deleteButton.classList.add('delete-button'); // 使用预定义的class
        deleteButton.onclick = function ()
        {
            const option = document.createElement('option');
            const word = mappingElement.getAttribute('cur_word');
            option.value = word;
            option.text = word;
            cur_sent_dropdown.appendChild(option);
            mappingElement.remove();
        };

        // 将文本和按钮添加到主div中
        mappingElement.appendChild(textContent);
        mappingElement.appendChild(deleteButton);

        // 将 mappingElement 添加到容器中
        mappingContainer.appendChild(mappingElement);

        removeOptionByValue(cur_sent_dropdown, cur_word);
    }


    function extractIndexes(cur_word, prev_word)
    {
        const [, index3, index4] = prev_word.match(/\((\d+),\s*(\d+)\)/) || [];
        const [, , index2] = cur_word.match(/\((\d+),\s*(\d+)\)/) || [];
        return index3 && index4 && index2 ? `(${index3}, ${index4}, ${index2})` : 'Invalid input format';
    }

    function removeOptionByValue(dropdown, value)
    {
        for (let i = 0; i < dropdown.options.length; i++)
        {
            if (dropdown.options[i].value === value)
            {
                dropdown.remove(i);
                break;
            }
        }
    }


    function processingData(data)
    {
        cleanMappingDiv();

        console.log(data.indexed_text.prev_text);
        indexedPrevText = data.indexed_text.prev_text;
        indexedCurText = data.indexed_text.cur_text;

        indexed_prev_sent.innerHTML = data['indexed_prev_text'];
        indexed_cur_sent.innerHTML = data['indexed_cur_text'];

        createDropDown(data['prev_possible_tokens'], prev_sent_dropdown);
        createDropDown(data['cur_possible_tokens'], cur_sent_dropdown);

    }

    function createDropDown(tokens, dropdown)
    {
        dropdown.innerHTML = '';
        tokens.forEach(token =>
        {
            const option = document.createElement('option');
            option.value = token;
            option.text = token;
            dropdown.appendChild(option);
        })
    }

    function cleanMappingDiv()
    {
        mappingContainer.innerHTML = "";
    }

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

});
