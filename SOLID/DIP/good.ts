export type User = {
  id: string;
  name: string;
};

export class UserController {
  constructor(private userService: IUserService) {
    this.userService = userService;
  }

  create(user: User): User {
    return this.userService.create(user);
  }

  findById(id: string): User {
    return this.userService.findById(id);
  }
}

export interface IUserService {
  create(user: User): User;
  findById(id: string): User;
}

export class UserService implements IUserService {
  constructor(private userRepository: IUserRepository) {
    this.userRepository = userRepository;
  }

  create(user: User): User {
    return this.userRepository.create(user);
  }

  findById(id: string): User {
    return this.userRepository.findById(id);
  }
}

export interface IUserRepository {
  create(user: User): User;
  findById(id: string): User;
}

export class UserRepository implements IUserRepository {
  create(user: User) {
    return {
      id: "ID001",
      name: "Tanaka",
    } as User;
  }

  findById(id: string): User {
    return {
      id: "ID001",
      name: "Tanaka",
    } as User;
  }
}

export class TestUserRepository implements IUserRepository {
  create(user: User) {
    return {
      id: "ID000",
      name: "test",
    } as User;
  }

  findById(id: string): User {
    return {
      id: "ID000",
      name: "test",
    } as User;
  }
}

function run() {
  const userRepository = new UserRepository();
  const userService = new UserService(userRepository);
  const userController = new UserController(userService);

  console.log(userController.findById("dummy"));
}

run();
