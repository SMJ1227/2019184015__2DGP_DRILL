from pico2d import *

# 이벤트 정의
# RD, LD, RU, LU = 0, 1, 2, 3
RD, LD, RU, LU, TIMER, AUTO = range(6)

# 키입력에 따른 상태
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): AUTO,
}

class IDLE:
    def enter(self, event): # 상태에 들어갈 때 행하는 액션
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000

    def exit(self): # 상태를 나올 때 하는 액션
        print('EXIT IDLE')

    def do(self): # 상태에 있을 때 지속적으로 행하는 액션
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

class RUN:
    def enter(self, event): # 상태에 들어갈 때 행하는 액션
        print("ENTER RUN")
        # 방향 결정. 눌려있는 키를 근거로 판단. 키 이벤트 정보가 필요.
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        elif event == SDLK_a:
            self.add_event(AUTO)

    def exit(self): # 상태를 나올 때 하는 액션
        print('EXIT RUN')
        self.face_dir = self.dir

    def do(self): # 상태에 있을 때 지속적으로 행하는 액션
        self.frame = (self.frame + 1) % 8
        # x좌표 변경, 달리기
        self.x += self.dir
        self.x = clamp(0, self.x, 800) #행동 제한

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class AUTO_RUN:
    def enter(self, event):
        print("ENTER AUTO_RUN")
        if self.face_dir == 1:
            self.dir = 1
        else:
            self.dir = -1

    def exit(self):
        print('EXIT AUTO_RUN')
        self.face_dir = self.dir
        self.dir = 0

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y + 25, 200, 200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y + 25, 200, 200)

class SLEEP:
    def enter(self, event):
        print('ENTER SLEEP')

    def exit(self):
        print('EXIT SLEEP')

    def do(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592/2, ' ',
                                           self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592/2, ' ',
                                           self.x - 25, self.y - 25, 100, 100)

# 상태 변환 기술
next_state = {
    SLEEP : {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AUTO: None},
    IDLE : {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AUTO: AUTO_RUN},
    RUN : {RU: IDLE, LU: IDLE, RD: RUN, LD: RUN, AUTO: AUTO_RUN},
    AUTO_RUN : {RU: None, LU: None, RD: RUN, LD: RUN, AUTO: IDLE}
}

class Boy:
    def add_event(self, event):
        self.q.insert(0, event)

    def handle_events(self, event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.q.insert(0, key_event)

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None) # 초기 상태의 entry액션 수행

    def update(self):
        self.cur_state.do(self) # 현재 상태의 do 액션 수행
        # 이벤트를 확인해서 이벤트가 있으면 이벤트 변환 처리
        if self.q: # 큐에 이벤트가 있으면
            event = self.q.pop()
            self.cur_state.exit(self) # 현재 상태를 나간다
            self.cur_state = next_state[self.cur_state][event] # 다음 상태를 구한다.
            self.cur_state.enter(self, event) # 다음 상태의 entry action 수행

    def draw(self):
        self.cur_state.draw(self)
