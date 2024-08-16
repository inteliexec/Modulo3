import http from 'k6/http';
import { sleep } from 'k6';
import { check } from 'k6';

export let options = {
    stages: [
        { duration: '1m', target: 40 },
        { duration: '2m', target: 25 },
        { duration: '1m', target: 0 },
    ],
};

export default function () {
    let res = http.get('https://inteli-exec-m3.streamlit.app/');
    check(res, {
        'status é 200': (r) => r.status === 200,
        'tempo de resposta < 1000ms': (r) => r.timings.duration < 1000,
    });
    sleep(1);
}
